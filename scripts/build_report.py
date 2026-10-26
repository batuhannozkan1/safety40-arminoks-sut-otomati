#!/usr/bin/env python3
"""Markdown kaynaklarından bölüm/birleşik PDF ve kaynaklı diyagramlar üretir."""
from pathlib import Path
import csv
import hashlib
import html
import json
import math
import os
import re
import textwrap
from sync_sources import generated_files

import fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    Image, KeepTogether,
)
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor('#132C46')
TEAL = colors.HexColor('#007F86')
RED = colors.HexColor('#A83F4B')
LIGHT = colors.HexColor('#EAF3F5')
GREY = colors.HexColor('#4B5C6D')
DOCS = [
    ('00-makine-profili.md', '00_Makine_Profili.pdf'),
    ('lab1-safety-architecture.md', 'LAB1_Safety_Architecture.pdf'),
    ('lab2-zone-conduit.md', 'LAB2_Zone_Conduit.pdf'),
    ('lab3-risk-register.md', 'LAB3_Risk_Register.pdf'),
    ('lab4-secure-remote-access.md', 'LAB4_Secure_Remote_Access.pdf'),
    ('lab5-vulnerability-decision.md', 'LAB5_Vulnerability_Decision.pdf'),
    ('06-swot-dogrulama.md', '06_SWOT_Dogrulama.pdf'),
    ('07-teslim-kontrolu.md', '07_Teslim_Kontrolu.pdf'),
]


def register_fonts():
    candidates = [
        Path(os.environ.get('ARMINOKS_FONT_DIR', 'fonts')),
        Path('/usr/share/fonts/truetype/dejavu'),
        Path('C:/Windows/Fonts'),
    ]
    for folder in candidates:
        regular = folder / 'DejaVuSans.ttf'
        bold = folder / 'DejaVuSans-Bold.ttf'
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont('Body', str(regular)))
            pdfmetrics.registerFont(TTFont('Body-Bold', str(bold)))
            pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold', italic='Body', boldItalic='Body-Bold')
            return
    raise SystemExit('DejaVuSans.ttf ve DejaVuSans-Bold.ttf gerekli. ARMINOKS_FONT_DIR ile dizini belirtin.')


def inline(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'\1', s)
    def link(m):
        label, url = m.groups()
        if url.startswith('https://'):
            return '<link href="' + url + '" color="#007F86">' + label + '</link>'
        return label
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, s)


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name='BodyTR', fontName='Body', fontSize=9.1, leading=14.2,
                         textColor=NAVY, spaceAfter=7, splitLongWords=True))
    s.add(ParagraphStyle(name='CellTR', fontName='Body', fontSize=7.5, leading=11,
                         textColor=NAVY, splitLongWords=True))
    s.add(ParagraphStyle(name='HeadCellTR', parent=s['CellTR'], fontName='Body-Bold', textColor=colors.white))
    for name, size, leading, before, after in [
        ('H1TR', 21, 27, 8, 17), ('H2TR', 13, 18, 14, 8), ('H3TR', 10.2, 15, 11, 6),
    ]:
        s.add(ParagraphStyle(name=name, fontName='Body-Bold', fontSize=size, leading=leading,
                             textColor=TEAL if name != 'H1TR' else NAVY,
                             spaceBefore=before, spaceAfter=after, keepWithNext=True))
    return s


def table(rows, st):
    # Keep headings with a readable opening chunk, not an entire long table.
    # A full table that happens to fit the next page otherwise leaves large gaps.
    if len(rows)>13:
        result=[]
        for start in range(1,len(rows),12):
            result.extend(table([rows[0]]+rows[start:start+12],st))
        return result
    cols = len(rows[0])
    clean = [r + [''] * (cols-len(r)) for r in rows]
    clean = [r[:cols] for r in clean]
    # Allocate space using observed text lengths, while preserving narrow ID columns.
    weights = []
    for i in range(cols):
        lengths = [len(re.sub(r'\[([^]]+)\]\([^)]+\)', r'\1', r[i])) for r in clean]
        weights.append(max(3.0, math.sqrt(min(max(lengths), 170))))
    available = A4[0] - 92
    widths = [available * w / sum(weights) for w in weights]
    data = [[Paragraph(inline(cell), st['HeadCellTR'] if n == 0 else st['CellTR'])
             for cell in r] for n, r in enumerate(clean)]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LINEBELOW', (0,0), (-1,0), 1, TEAL),
        ('LINEBELOW', (0,1), (-1,-1), .25, colors.HexColor('#D5E1E7')),
    ]))
    return [t, Spacer(1, 9)]


def parse_markdown(path, st):
    lines = path.read_text(encoding='utf-8').splitlines()
    result, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('!['):
            match = re.match(r'!\[([^]]+)\]\(([^)]+)\)', line)
            if match:
                image_path = (path.parent / match[2]).resolve()
                im = Image(str(image_path))
                scale = min((A4[0]-104)/im.imageWidth, 325/im.imageHeight)
                im.drawWidth, im.drawHeight = im.imageWidth*scale, im.imageHeight*scale
                result += [KeepTogether([im, Paragraph(inline(match[1]), st['CellTR']), Spacer(1, 8)])]
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                row = [x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[:\- ]+', x or '-') for x in row):
                    rows.append(row)
                i += 1
            result.extend(table(rows, st))
            continue
        if line.startswith('#'):
            level = len(line)-len(line.lstrip('#'))
            result.append(Paragraph(inline(line[level:].strip()), st[{1:'H1TR',2:'H2TR'}.get(level,'H3TR')]))
            i += 1
            continue
        if re.match(r'^\d+\. ', line):
            result.append(Paragraph(inline(line), st['BodyTR']))
            i += 1
            continue
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#|\||!\[|\d+\. )', lines[i].strip()):
            paragraph.append(lines[i].strip())
            i += 1
        result.append(Paragraph(inline(' '.join(paragraph)), st['BodyTR']))
    return result


def page_frame(c, doc):
    w,h = A4
    c.saveState()
    c.setFillColor(TEAL)
    c.rect(0,h-9,w,9,fill=1,stroke=0)
    c.setFont('Body-Bold',7.3)
    c.setFillColor(GREY)
    c.drawString(46,h-35,'SAFETY 4.0  /  ARMİNOKS SÜT OTOMATI')
    c.setStrokeColor(colors.HexColor('#CBD9E1'))
    c.line(46,42,w-46,42)
    c.setFont('Body',6.7)
    c.drawString(46,29,'Batuhan Yaşar Özkan  |  230541050  |  Eğitim analizi · Saha doğrulaması değildir')
    c.drawRightString(w-46,29,str(doc.page))
    c.restoreState()


def cover(st):
    return [Spacer(1,105), Paragraph('SAFETY 4.0',st['H2TR']),
            Paragraph('Arminoks<br/>Süt Otomatı',st['H1TR']),
            Paragraph('LAB 1–5 · Machine Starter Pack',st['H2TR']), Spacer(1,25),
            Paragraph('Batuhan Yaşar Özkan<br/>230541050 · Atama no: 35 · SAMİB<br/>26 Ekim 2026',st['BodyTR']),
            Spacer(1,25), Paragraph('Açık kaynaklı ürün bilgisi, açık varsayımlar ve izlenebilir gereksinimlerle hazırlanmış eğitim analizi.',st['BodyTR']),
            Spacer(1,18), Paragraph('İçerik: Makine profili · Emniyet mimarisi · Zone/conduit · Risk Register · Güvenli uzaktan erişim · Yama kararı · SWOT · Teslim kontrolü',st['BodyTR']),
            Spacer(1,20), Paragraph('<b>Kamuya açık ürün bilgilerine ve belirtilen ders kabullerine dayanır. Gerçek cihazda test yapılmamıştır.</b>',st['BodyTR']),PageBreak()]


def build_pdf(target, sources, full=False):
    st = styles()
    story = cover(st) if full else []
    for n, source in enumerate(sources):
        if n:
            story.append(PageBreak())
        story.extend(parse_markdown(source,st))
    doc = SimpleDocTemplate(str(target), pagesize=A4, rightMargin=46,leftMargin=46,
                             topMargin=53,bottomMargin=56,
                             title='Arminoks Süt Otomatı | Safety 4.0 LAB1–5',
                             author='Batuhan Yaşar Özkan')
    doc.build(story,onFirstPage=page_frame,onLaterPages=page_frame)
    if full:
        pdf=fitz.open(target)
        toc=[]
        for source in sources:
            heading=source.read_text(encoding='utf-8').splitlines()[0].lstrip('# ').strip()
            normalized=' '.join(heading.split())
            for n,page in enumerate(pdf):
                if n and normalized in ' '.join(page.get_text().split()):
                    toc.append([1,heading,n+1])
                    break
        pdf.set_toc(toc)
        out=target.with_suffix('.indexed.pdf')
        pdf.save(out,garbage=4,deflate=True)
        pdf.close()
        out.replace(target)


def box(c,x,y,w,h,title,body='',color=TEAL):
    c.setFillColor(color)
    c.roundRect(x,y,w,h,9,fill=1,stroke=0)
    c.setFillColor(colors.white)
    c.setFont('Body-Bold',10)
    c.drawCentredString(x+w/2,y+h-19,title)
    c.setFont('Body',8.3)
    for n,line in enumerate(body.split('\n')):
        c.drawCentredString(x+w/2,y+h-35-n*13,line)


def arrow(c,x1,y1,x2,y2,label='',color=GREY,dashed=False):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(1.5)
    c.setDash(4,3) if dashed else c.setDash()
    c.line(x1,y1,x2,y2)
    c.setDash()
    ang=math.atan2(y2-y1,x2-x1)
    a=7
    p=c.beginPath();p.moveTo(x2,y2)
    p.lineTo(x2-a*math.cos(ang-.45),y2-a*math.sin(ang-.45))
    p.lineTo(x2-a*math.cos(ang+.45),y2-a*math.sin(ang+.45));p.close()
    c.drawPath(p,fill=1,stroke=0)
    if label:
        c.setFont('Body',7.5)
        c.drawString((x1+x2)/2+6,(y1+y2)/2+4,label)


def diagram(name,title,draw):
    pdf=ROOT/'diagrams'/f'{name}.pdf'
    c=canvas.Canvas(str(pdf),pagesize=(720,520))
    c.setFillColor(colors.HexColor('#F3F7FA'));c.rect(0,0,720,520,fill=1,stroke=0)
    c.setFillColor(NAVY);c.setFont('Body-Bold',17);c.drawString(30,485,title)
    draw(c)
    c.setFillColor(GREY);c.setFont('Body',8)
    c.drawString(30,17,'D: doğrulanan özellik · V: eğitim varsayımı · H: hedef gereksinim | Gerçek kurulum şeması değildir')
    c.save()
    d=fitz.open(pdf); pix=d[0].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False)
    pix.save(ROOT/'diagrams'/f'{name}.png');d.close()


def diagrams():
    def l1(c):
        box(c,30,350,280,84,'NORMAL KONTROL [V01]','Panel / sensör → normal mantık\nSatış, karıştırma, soğutma, yıkama',NAVY)
        box(c,410,350,280,84,'BAKIM GİRİŞLERİ [D/V]','USB satış kaydı [D05]\nUzak yazma / paket yükleme [V05/V08]',GREY)
        arrow(c,410,390,310,390,'yazma [V]')
        box(c,30,195,280,91,'EMNİYET SINIRI [H01/H03]','Kapak / duruş bilgisi → koruma mantığı\n→ tehlikeli hareketi engelle',RED)
        box(c,410,195,280,91,'ÜRÜN / PROSES KORUMA [H02/H04]','Geçerli sıcaklık ve ürün uygunluğu\nYıkama-satış dışlaması',TEAL)
        arrow(c,170,350,170,286,'komut korumayı aşamaz',dashed=True)
        arrow(c,550,350,550,286,'ayar yolu sınırlandırılır',dashed=True)
        box(c,170,63,380,72,'İŞLEV BAZLI GÜVENLİ DURUM [H]','Tehlikeli hareket / satış engelli\nGüvenli soğutma korunur; bakım izolasyonu ayrı',NAVY)
        arrow(c,170,195,270,135)
        arrow(c,550,195,450,135)
    diagram('lab1-mimari','LAB 1 · Normal kontrol ve hedef koruma',l1)
    def l2(c):
        box(c,30,360,250,80,'Z0 DIŞ SERVİS [V05]','Servis / internet / dış dosya kaynağı',GREY)
        box(c,440,360,250,80,'Z1 İŞLETME [D08/V]','Varsa ödeme / işletme ağı',GREY)
        box(c,30,230,250,80,'Z2 BAKIM GEÇİDİ [H06]','VPN · MFA · jump server\nKişisel hesap · süre · kayıt',TEAL)
        box(c,440,230,250,80,'Z3 BAKIM [V/H]','Bakım istasyonu\nOnaylı paket / proje',TEAL)
        box(c,30,80,250,90,'Z4 NORMAL KONTROL [V01]','Panel / kontrolör / proses çıkışları\nUSB [D05]; aktarım kontrolü [H05]',NAVY)
        box(c,440,80,250,90,'Z5 KORUMA [H01–H04]','Bağımsız işlev sınırı\nUzak programlama izni yok',RED)
        arrow(c,155,360,155,310,'C01')
        arrow(c,280,270,440,270,'C02')
        arrow(c,480,230,250,170,'C03')
        c.setStrokeColor(GREY);c.setLineWidth(1.5);c.setDash(4,3)
        c.lines([(690,400,705,400),(705,400,705,56),(705,56,155,56)])
        c.setDash()
        arrow(c,155,56,155,80,'C06',dashed=True)
        arrow(c,440,120,280,120,'C05')
        c.setFillColor(GREY);c.setFont('Body',8)
        c.drawString(32,35,'C04: USB → Z4 kontrollü aktarım. C07: opsiyonel SMS yalnız bildirim; komut yolu değildir.')
    diagram('lab2-zonlar','LAB 2 · Hedef zone / conduit modeli',l2)
    def l3(c):
        c.setFillColor(GREY);c.setFont('Body',10)
        c.drawString(45,440,'S=3 için Skor = L × 3 × E. Renk banttır; her hücre S3 bayrağını korur.')
        for i,L in enumerate([3,2,1]):
            c.setFillColor(NAVY);c.setFont('Body-Bold',12);c.drawString(45,348-i*95,f'L={L}')
            for j,E in enumerate([1,2,3]):
                score=L*3*E
                color=RED if score>=18 else colors.HexColor('#BD7433') if score>=9 else TEAL if score>=4 else GREY
                box(c,120+j*180,307-i*95,158,75,f'{score}  ·  S3',f'E={E}',color)
        c.setFillColor(NAVY);c.setFont('Body',10)
        c.drawString(45,73,'R-01: 27 | R-02: 6 | R-03: 3 | R-04: 3')
        c.drawString(45,49,'S3: Ağır fiziksel sonuç olasılığı düşük skorla gizlenmez; doğrulama bekler.')
    diagram('lab3-matris','LAB 3 · S3 dilimi ve öncelik',l3)
    def l4(c):
        box(c,30,355,280,85,'BAŞLANGIÇ [V05/V06]','Sürekli açık dış servis\nVarsayılan kimlik / sınırsız yazma',GREY)
        box(c,30,212,280,83,'NORMAL KONTROL [V08]','Kapak ve yeniden başlama\nnormal yazılıma bağlı',RED)
        arrow(c,170,355,170,295,'G01 → G05')
        box(c,410,355,280,85,'HEDEF GİRİŞ [H06]','VPN + MFA + kişisel hesap\nJump server / süre / kayıt',TEAL)
        box(c,410,212,280,83,'SINIRLI BAKIM [H05/H06]','Yalnız onaylı normal kontrol değişikliği\nKoruma programlamasına uzak yazma yok',TEAL)
        arrow(c,550,355,550,295,'C01–C03')
        box(c,410,64,280,82,'BAĞIMSIZ KORUMA [H01–H04]','Giriş aşılsa bile\nkoruma kararı geçersiz kılınamaz',NAVY)
        arrow(c,550,212,550,146,'ayrı doğrulama gerekir',dashed=True)
        c.setFillColor(NAVY);c.setFont('Body',9)
        for n,line in enumerate(['Başlangıç, gerçek Arminoks bulgusu değildir.','Hedef öneri kurulmuş/test edilmiş sayılmaz.','R-01 zinciri hem girişte hem etkide kesilir.']):
            c.drawString(30,138-n*18,line)
    diagram('lab4-erisim','LAB 4 · Başlangıçtan hedef gereksinime',l4)
    def l5(c):
        box(c,180,361,360,79,'ÜÇ KOŞULU DOĞRULA','Bileşen var mı? Sürüm etkileniyor mu?\nİlgili açık ulaşılabilir mi?',NAVY)
        box(c,30,210,200,83,'BİLİNMİYOR','VD-01: inceleme bekliyor\nGüvenli devam varsayılmaz',GREY)
        box(c,260,210,200,83,'KANITLA KAPSAM DIŞI','Gerekçe ve kanıtı kaydet\nDeğişiklikte yeniden incele',TEAL)
        box(c,490,210,200,83,'ETKİLENİYOR','Geçici önlem + güvenli durum\nYama ve etki analizi',RED)
        arrow(c,270,361,130,293)
        arrow(c,360,361,360,293)
        arrow(c,450,361,590,293)
        box(c,180,62,360,83,'TEST → YETKİLİ KABUL → İZLEME','Yedek / geri dönüş + D01–D07\nBaşarısızsa güvenli duruma dön; kapanış yok',NAVY)
        arrow(c,590,210,500,145)
        arrow(c,130,210,220,145,'kanıt tamamlanırsa')
    diagram('lab5-karar','LAB 5 · Zafiyet ve yama kararı',l5)


def main():
    register_fonts()
    for name, content in generated_files().items():
        (ROOT/name).write_text(content,encoding='utf-8',newline='\n')
    (ROOT/'diagrams').mkdir(exist_ok=True)
    (ROOT/'pdf').mkdir(exist_ok=True)
    diagrams()
    for source,target in DOCS:
        build_pdf(ROOT/'pdf'/target,[ROOT/'docs'/source])
    build_pdf(ROOT/'pdf'/'Arminoks_Sut_Otomati_LAB1-5_Rapor.pdf',
              [ROOT/'docs'/source for source,_ in DOCS],True)
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted((ROOT/'docs').glob('*.md'))}
    (ROOT/'data'/'source_hashes.json').write_text(json.dumps(hashes,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('PDF ve diyagramlar üretildi: '+str(ROOT/'pdf'))


if __name__=='__main__':
    main()
