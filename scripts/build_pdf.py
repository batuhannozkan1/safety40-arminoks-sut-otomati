"""Build föy-style PDFs from labs/*.md.

Usage: python scripts/build_pdf.py
Needs: pip install -r requirements.txt, a Chromium/Chrome binary (set CHROME=/path if not found),
and network access on first run (pinned static fonts + mermaid, cached under ~/.cache/arminoks-foy).
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

import markdown
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / 'labs'
PDF = ROOT / 'pdf'
CSS = Path(__file__).with_name('foy.css')
CACHE = Path.home() / '.cache' / 'arminoks-foy'
MERMAID_URL = 'https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js'
REPO_URL = 'https://github.com/batuhannozkan1/safety40-arminoks-sut-otomati/blob/main/'

STUDENT = {'Ad Soyad': 'Batuhan Yaşar Özkan', 'Öğrenci No': '230541050',
           'Grup': 'Gündüz-B', 'Tarih': '06.11.2026'}
MACHINE = 'Arminoks Süt Otomatı'

# Teacher's föy questions (2.1 lab_foyleri_genel.pdf), verbatim. Each must appear in its PDF.
FOY = {
    '1': ['Bu makinede tehlike nedir? İnsan neyden zarar görür?',
          'Safety function (emniyet fonksiyonu) hangisidir?',
          'Safety-related control system nerede? Şemada işaretleyin.',
          'Normal PLC ile Safety PLC farkı nedir?',
          'PLr / SIL neden var? Bu fonksiyon için neden önemli?',
          'Safe state (güvenli durum) nedir?',
          'Safety function hangi dijital bağımlılıklara sahip?',
          'Siber müdahale hangi noktadan bu fonksiyonu bozar?'],
    '2': ['Hangi varlıklar aynı bölgede? Bölgeleri adlandırıp gruplandırın.',
          "Safety PLC'yi hangi bölgeye koydunuz — neden?",
          'Bölgeler arası geçişler (conduit) nerede? Her geçişte ne kontrol edilecek?',
          'Aracı? Doğrudan / Jump server', 'Tünel? Açık / VPN', 'Kimlik? Parola / MFA',
          'Hesap? Paylaşılan / Kişisel', 'Kayıt? Yok / Tam oturum kaydı',
          'Zamanlama? Sürekli açık / Varsayılan kapalı'],
    '3': ['En yüksek öncelikli senaryonuz hangisi? Bir cümleyle: neden bu?',
          'S=3 olup skoru düşük kalan senaryonuz var mı? Nasıl görünür kılacaksınız?'],
    '4': ['Saldırgan tüm önlemlere rağmen içeri girerse: emniyet fonksiyonu etkilenir mi? Neden?',
          'Emniyet fonksiyonunun kontrol sisteminden bağımsız çalışması için GEREKSİNİMİ yazın (çözümü değil).'],
    '5': ['Bu CVE sizi gerçekten etkiliyor mu? (üç şartı kontrol edin)',
          'Üretimi hemen durdurur musunuz? Neden / neden değil?',
          'Yamayı doğrudan mı uygularsınız, önce test mi? Nerede test?',
          'Bu yama bir safety validation etkiliyor mu? Nasıl anlarsınız?',
          'Yama mümkün değilse compensating control (telafi edici önlem) ne olur?'],
    '6': ['10:15 — ilk 15 dk: Kimi ararsınız? İlk üç eyleminiz?',
          'İlk 2 saat: Emniyet güvende mi? Neyi korursunuz (kanıt!)? Hangi hesap kapatılır?',
          '24 saat — CRA erken uyarı: Hangi bilgi hazır olmalı?',
          '72 saat — CRA bildirim: Kök neden, etki, önlem — kim ne yapıyor?',
          '14 gün — son rapor: Hangi loglar/kayıtlar korunmuş olmalı?'],
    '7': ['Model yanlış sınıflandırdı:', 'Girdi manipüle edildi:', 'Confidence düştü:',
          'Eşik ne olmalı? Altında: dur / insana sor / fallback?'],
}
EXTRA_PER_LAB = 4

META_RE = re.compile(r'<!--\s*foy\s+(.*?)-->', re.S)
SKIP_RE = re.compile(r'<!--\s*pdf:skip-start\s*-->.*?<!--\s*pdf:skip-end\s*-->', re.S)
MERMAID_RE = re.compile(r'```mermaid\n(.*?)```', re.S)


def fail(msg):
    sys.exit('HATA: ' + msg)


def fetch(url, target):
    """Download atomically so an interrupted download never poisons the cache."""
    if target.exists():
        return target
    CACHE.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(target.suffix + '.part')
    urllib.request.urlretrieve(url, tmp)
    os.replace(tmp, target)
    return target


def find_chrome():
    env = os.environ.get('CHROME')
    if env:
        if not Path(env).exists():
            fail(f'CHROME={env} bulunamadı.')
        return env
    # chrome-headless-shell first: full Chrome's --headless print can hang on WSL/servers.
    cands = []
    cands += sorted(Path.home().glob('.cache/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell'), reverse=True)
    cands += sorted(Path.home().glob('.cache/ms-playwright/chromium-*/chrome-linux*/chrome'), reverse=True)
    cands += [shutil.which(n) for n in ('chromium', 'chromium-browser', 'google-chrome', 'chrome')]
    cands += ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
              r'C:\Program Files\Google\Chrome\Application\chrome.exe']
    for c in cands:
        if c and Path(c).exists():
            return str(c)
    fail('Chrome/Chromium bulunamadı; CHROME=/yol/chrome ile belirtin.')


def mermaid_js():
    return fetch(MERMAID_URL, CACHE / 'mermaid-11.4.1.min.js')


FONT_URL = 'https://cdn.jsdelivr.net/npm/@fontsource/{fam}@5.1.0/files/{fam}-{sub}-{w}-normal.woff2'
FONTS = {'Inter': ('inter', (400, 500, 600, 700)), 'Lora': ('lora', (600, 700))}
RANGES = {  # static per-weight files: variable fonts make Chrome emit bulky Type3 glyphs
    'latin': 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,'
             'U+0329,U+2000-206F,U+20AC,U+2122,U+2190-2193,U+2212,U+2215,U+FEFF,U+FFFD',
    'latin-ext': 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+1E00-1E9F,'
                 'U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF',
}


def fonts_css():
    rules = []
    for family, (fam, weights) in FONTS.items():
        for w in weights:
            for sub, rng in RANGES.items():
                path = fetch(FONT_URL.format(fam=fam, sub=sub, w=w), CACHE / f'{fam}-{sub}-{w}.woff2')
                rules.append(f"@font-face{{font-family:'{family}';font-weight:{w};font-style:normal;"
                             f"src:url('{path.as_uri()}') format('woff2');unicode-range:{rng};}}")
    return '\n'.join(rules)


def parse(md_path):
    text = md_path.read_text(encoding='utf-8')
    m = META_RE.search(text)
    if not m:
        fail(f'{md_path.name}: <!-- foy ... --> bilgisi yok')
    meta = dict(re.findall(r'(\w+)="([^"]*)"', m.group(1)))
    body = SKIP_RE.sub('', META_RE.sub('', text))
    body = MERMAID_RE.sub(lambda g: '<pre class="mermaid">' + html.escape(g.group(1)) + '</pre>', body)
    # Python-Markdown merges blank-line-separated quotes; keep them separate as GitHub does
    body = re.sub(r'^(>.*\n)\n(?=>)', r'\1\n<div></div>\n\n', body, flags=re.M)
    return meta, body


def to_html(body):
    out = markdown.markdown(body, extensions=['tables', 'attr_list', 'md_in_html', 'sane_lists'])
    out = out.replace('<code>EK SORU</code>', '<span class="badge ek">EK SORU</span>')
    out = out.replace('<code>UYARLANDI</code>', '<span class="badge ad">UYARLANDI</span>')
    out = out.replace('<code>DERS NOTU</code>', '<span class="badge dn">DERS NOTU</span>')
    out = re.sub(r'<h3>(\d+)\.\s*(.*?)</h3>',
                 r'<h3 class="q"><span class="num">\1</span><span class="qt">\2</span></h3>', out)
    # indent each answer: wrap everything after a numbered question up to the next heading
    out = re.sub(r'(<h3 class="q">.*?</h3>)(.*?)(?=<h[23][ >]|\Z)',
                 r'<section class="qa">\1<div class="answer">\2</div></section>', out, flags=re.S)

    def quote(m):
        inner = m.group(1)
        plain = re.sub('<[^>]+>', '', inner).strip()
        cls = 'note'
        if plain.startswith('Kavram'):
            cls = 'concept'
        elif plain.startswith('Arminoks bağlamı'):
            cls = 'context'
        elif plain.startswith('Bu föyün çıktısı'):
            cls = 'output'
        return f'<blockquote class="{cls}">{inner}</blockquote>'
    out = re.sub(r'<blockquote>(.*?)</blockquote>', quote, out, flags=re.S)
    out = re.sub(r'<h2>(.*?)</h2>', r'<h2><span>\1</span></h2>', out)
    # links to other repo files keep working from the PDF folder (GitHub relative paths)
    out = re.sub(r'href="(\.\./)?(raporlar|pdf|labs)/', rf'href="{REPO_URL}\2/', out)
    out = re.sub(r'href="(?!https?://|#)([^"/]+\.md)"', rf'href="{REPO_URL}labs/\1"', out)
    return out


def page_html(meta, content, mermaid):
    lab = meta.get('lab', '')
    kicker = f'LABORATUVAR {lab} · {MACHINE}' if lab.isdigit() else f'{meta.get("kicker", "BAŞLANGIÇ")} · {MACHINE}'
    footer_label = f'Lab {lab}' if lab.isdigit() else meta.get('short', 'Profil')
    ident = ''.join(f'<div><span>{k}</span><b>{v}</b></div>' for k, v in STUDENT.items())
    css = CSS.read_text(encoding='utf-8')
    return f'''<!doctype html><html lang="tr"><head><meta charset="utf-8">
<title>{html.escape(meta["title"])} — {MACHINE}</title>
<style>{fonts_css()}
{css}
@page {{ @bottom-right {{ content: "{footer_label} · " counter(page) " / " counter(pages); }} }}
</style></head><body>
<header class="band"><div class="kicker">{html.escape(kicker.upper())}</div>
<div class="row"><h1>{html.escape(meta["title"])}</h1>
<div class="pill">Çıktı: {html.escape(meta["output"])}</div></div></header>
<section class="ident">{ident}</section>
<main>{content}</main>
<script src="{mermaid.as_uri()}"></script>
<script>mermaid.initialize({{startOnLoad:true, theme:'base', securityLevel:'loose',
 themeVariables:{{fontFamily:'Inter', fontSize:'13px', primaryColor:'#e8eff6', primaryBorderColor:'#8fa6bd',
 lineColor:'#5b6f86', clusterBkg:'#f6f8fb', clusterBorder:'#b7c6d6'}},
 flowchart:{{htmlLabels:true, curve:'basis', padding:10}}}});</script>
</body></html>'''


def print_pdf(chrome, html_text, target):
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / 'foy.html'
        src.write_text(html_text, encoding='utf-8')
        cmd = [chrome, '--no-sandbox', '--no-pdf-header-footer', '--virtual-time-budget=15000',
               '--run-all-compositor-stages-before-draw',
               f'--user-data-dir={tmp}/profile', f'--print-to-pdf={target}', src.as_uri()]
        if 'headless-shell' not in chrome:
            cmd.insert(1, '--headless=new')
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            fail(f'{target.name}: Chrome 120 sn içinde bitmedi; CHROME ile chrome-headless-shell gösterin.')
        if r.returncode != 0 or not target.exists():
            fail(f'{target.name} üretilemedi (kod {r.returncode}): {r.stderr[-500:]}')
    doc = pymupdf.open(target)  # Chrome embeds whole fonts; subset + compress (~4x smaller)
    doc.subset_fonts()
    doc.set_metadata({'title': target.stem, 'author': STUDENT['Ad Soyad']})
    doc.ez_save(str(target) + '.tmp')
    doc.close()
    os.replace(str(target) + '.tmp', target)


def norm(s):
    return re.sub(r'\s+', ' ', s.replace('\u00ad', '')).strip()


def check(md_path, meta, content, pdf_path):
    errors = []
    doc = pymupdf.open(pdf_path)
    text = norm(' '.join(p.get_text() for p in doc))
    pos = -1
    for q in FOY.get(meta.get('lab', ''), []):
        at = text.find(norm(q), pos + 1)
        if at < 0:
            errors.append(f'föy sorusu PDF\'te yok ya da sırası bozuk: {q}')
        else:
            pos = at
    if 'Syntax error' in text or 'mermaid version' in text:
        errors.append('mermaid sözdizimi hatası')
    if meta.get('lab', '').isdigit():
        n = content.count('class="badge ek"')
        if n != EXTRA_PER_LAB:
            errors.append(f'EK SORU sayısı {n}, beklenen {EXTRA_PER_LAB}')
    if 'flowchart' in text or 'classDef' in text:
        errors.append('mermaid şeması çizilmemiş (ham metin PDF\'te)')
    for link in re.findall(r'\]\((?!https?://|#)([^)]+)\)', md_path.read_text(encoding='utf-8')):
        if not (md_path.parent / link.split('#')[0]).resolve().exists():
            errors.append(f'kırık bağlantı: {link}')
    return errors


def main():
    chrome = find_chrome()
    mermaid = mermaid_js()
    PDF.mkdir(exist_ok=True)
    built, errors = [], []
    for md_path in sorted(LABS.glob('*.md')):
        meta, body = parse(md_path)
        content = to_html(body)
        target = PDF / (md_path.stem + '.pdf')
        if target.exists():
            target.unlink()
        print_pdf(chrome, page_html(meta, content, mermaid), target)
        errs = check(md_path, meta, content, target)
        errors += [f'{md_path.name}: {e}' for e in errs]
        built.append((meta, target))
        print(f'{target.relative_to(ROOT)}  {pymupdf.open(target).page_count} sayfa  {"OK" if not errs else "HATA"}')
    combined = pymupdf.open()
    toc = []
    for meta, target in built:
        toc.append([1, (f'Lab {meta["lab"]} · ' if meta['lab'].isdigit() else '') + meta['title'],
                    combined.page_count + 1])
        combined.insert_pdf(pymupdf.open(target))
    combined.set_toc(toc)
    combined.set_metadata({'title': f'{MACHINE} — Safety 4.0 Laboratuvar Föyleri',
                           'author': STUDENT['Ad Soyad']})
    out = PDF / '00-tum-foyler.pdf'
    combined.save(out, garbage=4, deflate=True)
    print(f'{out.relative_to(ROOT)}  {combined.page_count} sayfa')
    readme = ROOT / 'README.md'
    for link in re.findall(r'\]\((?!https?://|#)([^)]+)\)', readme.read_text(encoding='utf-8')):
        if not (ROOT / link.split('#')[0]).exists():
            errors.append(f'README: kırık bağlantı: {link}')
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print('Öz kontrol: tüm föy soruları, ek soru sayıları ve bağlantılar tamam.')


if __name__ == '__main__':
    main()
