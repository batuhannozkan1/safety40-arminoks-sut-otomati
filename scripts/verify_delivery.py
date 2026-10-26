#!/usr/bin/env python3
"""Belge bütünlüğü ve eğitim modeli kontrolü; makine emniyeti testi değildir."""
from pathlib import Path
import hashlib
import json
import re
import sys
import fitz
from sync_sources import generated_files, BASE_IDS, EXTRA_IDS

ROOT=Path(__file__).resolve().parents[1]


def main():
    checks=[]
    def check(name,ok,detail=''):
        checks.append({'check':name,'passed':bool(ok),'detail':detail})
    manifest=json.loads((ROOT/'data/question_manifest.json').read_text())
    check('expected_question_set',set(manifest['questions'])==set(BASE_IDS+EXTRA_IDS))
    check('no_upload_guide',not (ROOT/'GITHUB-YUKLEME.md').exists() and 'GITHUB-YUKLEME' not in (ROOT/'README.md').read_text())
    check('no_windows_metadata',not any(p.name.endswith(':Zone.Identifier') for p in ROOT.rglob('*')))
    for name,expected in generated_files().items():
        check('generated_data:'+name,(ROOT/name).read_text(encoding='utf-8')==expected)
    for q in manifest['mandatory_and_course_discussion']+manifest['extra_questions']:
        p=ROOT/manifest['questions'][q]['file']
        text=p.read_text()
        match=re.search(r'^#{2,3} '+re.escape(q)+r' \|[^\n]*\n(.*?)(?=\n#{1,3} |\Z)',text,re.S|re.M)
        if manifest['questions'][q].get('format')=='table':
            match=re.search(r'^\| '+re.escape(q)+r' [^\n]+$',text,re.M)
            check('question:'+q,bool(match and len(match[0])>45))
        else:
            check('question:'+q,bool(match and len(match[1].strip())>45))
    riskdata=json.loads((ROOT/'data/risk_register.json').read_text())['risks']
    check('risk_count_and_profiles',len(riskdata)>=3 and len({r['profile'] for r in riskdata})>=3)
    inv=(ROOT/'docs/lab2-zone-conduit.md').read_text()
    sf=(ROOT/'docs/lab1-safety-architecture.md').read_text()
    for r in riskdata:
        check(r['id']+':score',r['score']==r['L']*r['S']*r['E'] and all(1<=r[k]<=3 for k in ['L','S','E']))
        check(r['id']+':s3',r['s3']==(r['S']==3))
        target=r['target_score']
        check(r['id']+':target_score',target['score']==target['L']*target['S']*target['E'])
        check(r['id']+':references',all(g in inv for g in r['gates']) and all(f in sf for f in r['safety_functions']) and all(c in inv for c in r['conduits']))
        check(r['id']+':scenario_links',bool(r['gates'] and r['safety_functions']))
        check(r['id']+':reasoning',all(k in r['justifications'] for k in ['L'+str(r['L'])+':','S'+str(r['S'])+':','E'+str(r['E'])+':']))
        check(r['id']+':management',bool(r['owner_accountable'] and r['target_date'] and r['evidence']))
    check('five_gates',len(set(re.findall(r'\| (G\d\d) \|',inv)))>=5)
    for p in ROOT.rglob('*.md'):
        for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text()):
            if not re.match(r'^[a-z]+://',link):
                target=(p.parent/link.split('#')[0]).resolve()
                check('link:'+str(p.relative_to(ROOT))+':'+link,target.exists())
    hashes=json.loads((ROOT/'data/source_hashes.json').read_text())
    for path,digest in hashes.items():
        check('source_hash:'+path,hashlib.sha256((ROOT/path).read_bytes().replace(b'\r\n',b'\n')).hexdigest()==digest)
    pdfs=sorted((ROOT/'pdf').glob('*.pdf'))
    check('pdf_count',len(pdfs)==9,str(len(pdfs)))
    for p in pdfs:
        doc=fitz.open(p)
        check('pdf_text:'+p.name,all(len(page.get_text().strip())>70 for page in doc))
        content=' '.join(page.get_text() for page in doc)
        match=re.match(r'LAB([1-5])_',p.name)
        if match:
            prefix='L'+match[1]+'-'
            check('pdf_questions:'+p.name,all(q in content for q in BASE_IDS+EXTRA_IDS if q.startswith(prefix)))
        if p.name=='Arminoks_Sut_Otomati_LAB1-5_Rapor.pdf':
            check('pdf_all_questions',all(q in content for q in BASE_IDS+EXTRA_IDS))
            check('pdf_bookmarks',len(doc.get_toc())==8)
        outside=[]
        replacement=[]
        for n,page in enumerate(doc):
            for block in page.get_text('dict')['blocks']:
                if 'lines' not in block:
                    continue
                for line in block['lines']:
                    for span in line['spans']:
                        x0,y0,x1,y1=span['bbox']
                        if x0<-0.5 or y0<-0.5 or x1>page.rect.width+0.5 or y1>page.rect.height+0.5:
                            outside.append(n+1)
                        if '\ufffd' in span['text']:
                            replacement.append(n+1)
        check('pdf_bounds:'+p.name,not outside,str(outside))
        check('pdf_glyphs:'+p.name,not replacement,str(replacement))
        doc.close()
    passed=sum(c['passed'] for c in checks)
    output={'passed':passed,'total':len(checks),'failed':[c for c in checks if not c['passed']],
            'limits':'Dosya/aritmetik kontrolüdür; gerçek cihaz veya emniyet doğrulaması değildir.', 'checks':checks}
    (ROOT/'data/verification.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(f'{passed}/{len(checks)} belge kontrolü geçti.')
    if output['failed']:
        print(json.dumps(output['failed'],ensure_ascii=False,indent=2))
        sys.exit(1)


if __name__=='__main__':
    main()
