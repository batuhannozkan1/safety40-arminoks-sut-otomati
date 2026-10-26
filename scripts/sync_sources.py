#!/usr/bin/env python3
"""Markdown'daki soru ve risk kayıtlarından yardımcı verileri günceller."""
from pathlib import Path
import argparse
import csv
import io
import json
import re

ROOT=Path(__file__).resolve().parents[1]
BASE_IDS=([f'L1-Q{i}' for i in range(1,9)]+[f'L2-A{i}' for i in range(1,4)]+
          [f'L2-B{i}' for i in range(1,7)]+['L2-P1','L3-Q1','L3-Q2']+
          [f'L3-T{i}' for i in range(1,6)]+['L4-A','L4-B1','L4-B2']+
          [f'L5-Q{i}' for i in range(1,6)])
EXTRA_IDS=[f'L{lab}-E{i}' for lab in range(1,6) for i in range(1,5)]


def json_text(value):
    return json.dumps(value,ensure_ascii=False,indent=2)+'\n'


def generated_files():
    questions={}
    for p in sorted((ROOT/'docs').glob('lab*.md')):
        text=p.read_text(encoding='utf-8')
        for q,title in re.findall(r'^#{2,3} (L\d-[A-Z]+\d*) \| (.+)$',text,re.M):
            if q in questions:
                raise ValueError('Tekrarlanan soru: '+q)
            questions[q]={'file':str(p.relative_to(ROOT)),'question':title}
        for q,title in re.findall(r'^\| (L2-B[1-6]) ([^|]+)\|',text,re.M):
            questions[q]={'file':str(p.relative_to(ROOT)),'question':title.strip()+': seçim ve gerekçe','format':'table'}
    missing=set(BASE_IDS+EXTRA_IDS)-questions.keys()
    if missing:
        raise ValueError('Eksik sorular: '+', '.join(sorted(missing)))
    manifest={'mandatory_and_course_discussion':BASE_IDS,'extra_questions':EXTRA_IDS,'questions':questions,
              'notes':['L2-P1 uyarlama sorusu; L3-T1-T5 ders tartışmasıdır.','LAB6-7 kapsam dışıdır.']}
    text=(ROOT/'docs/lab3-risk-register.md').read_text(encoding='utf-8')
    scores={}
    management={}
    for line in text.splitlines():
        cells=[x.strip() for x in line.strip().strip('|').split('|')]
        if not re.fullmatch(r'R-\d\d',cells[0]):
            continue
        if len(cells)==7:
            scores[cells[0]]=cells
        elif len(cells)==5:
            management[cells[0]]=cells
    risks=[]
    for rid,row in scores.items():
        match=re.search(r'^### '+rid+r' \| (.*?)\n\n(.*?)(?=\n#{2,3} |\Z)',text,re.M|re.S)
        title,body=match.groups()
        paragraphs=body.strip().split('\n\n')
        scenario,reasons=paragraphs[:2]
        l,s,e=map(int,row[1:4])
        declared_score=int(re.match(r'\d+',row[4])[0])
        if declared_score!=l*s*e:
            raise ValueError('Puan çarpımı yanlış: '+rid)
        mgmt=management[rid]
        target=re.search(r'(\d)/(\d)/(\d)\s*=\s*(\d+)',mgmt[4])
        tl,ts,te,score=map(int,target.groups())
        if score!=tl*ts*te:
            raise ValueError('Hedef çarpımı yanlış: '+rid)
        risks.append({'id':rid,'profile':title.split(':',1)[0],
                      'gates':sorted(set(re.findall(r'\bG\d\d\b',scenario))),
                      'safety_functions':sorted(set(re.findall(r'\bSF-\d\d\b',scenario))),
                      'conduits':sorted(set(re.findall(r'\bC\d\d\b',scenario))),
                      'L':l,'S':s,'E':e,'score':declared_score,'s3':row[5]=='Evet',
                      'priority':int(row[6]),'target_date':mgmt[3],
                      'target_score':{'L':tl,'S':ts,'E':te,'score':score,'status':'hedef; uygulanmadı'},
                      'scenario':scenario,'justifications':reasons,'action':mgmt[1],
                      'status':'Taslak; saha doğrulaması yapılmadı','owner_accountable':mgmt[2],
                      'evidence':'EP04 / LAB1 / LAB2 / KT01-KT07'})
    riskdata={'analysis_version':'1.1','date':'2026-10-26',
              'exposure_definition':'Yolun dışarıya açıklığı; insan maruziyeti değil','risks':risks}
    stream=io.StringIO(newline='')
    writer=csv.DictWriter(stream,fieldnames=['id','profile','L','S','E','score','s3','priority','target_date','status','scenario','justifications'],lineterminator='\n')
    writer.writeheader()
    writer.writerows({k:r[k] for k in writer.fieldnames} for r in risks)
    return {'data/question_manifest.json':json_text(manifest),'data/risk_register.json':json_text(riskdata),
            'data/risk_register.csv':'\ufeff'+stream.getvalue()}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    for name,content in generated_files().items():
        p=ROOT/name
        if args.check:
            if not p.exists() or p.read_text(encoding='utf-8')!=content:
                stale.append(name)
        else:
            p.write_text(content,encoding='utf-8',newline='\n')
    if stale:
        raise SystemExit('Kaynakla uyuşmayan veri: '+', '.join(stale))
    print('Soru ve risk verileri '+('kaynaklarla tutarlı.' if args.check else 'güncellendi.'))


if __name__=='__main__':
    main()
