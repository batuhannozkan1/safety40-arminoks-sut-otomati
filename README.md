# Safety 4.0 Bootcamp — Arminoks Süt Otomatı

Safety 4.0 Readiness Bootcamp laboratuvar föylerinin **Arminoks süt otomatına** uyarlanmış hâli. Her föy, öğretmenin genel föyündeki görevleri **aynı sırayla ve aynı soru metniyle** yanıtlar; sonuna makineye özgü 4 ek soru ekler. Föyler hem **Markdown** (GitHub'da okunur) hem **PDF** (föy tasarımında, yazdırılabilir) olarak bulunur.

| Ad Soyad | Öğrenci No | Grup | Tarih |
|---|---|---|---|
| Batuhan Yaşar Özkan | 230541050 | Gündüz-B | 06.11.2026 |

## Önce bu üç rapor

| Dosya | İçerik |
|---|---|
| **[Yazılım, sürüm ve CVE envanteri — Excel](raporlar/Arminoks_Yazilim_Surum_CVE_Envanteri.xlsx)** | Yazılım referansları, kurulu sürüm durumu, etkilenen sürüm koşulları, kanıtlar |
| **[Siber güvenlik ön değerlendirme raporu — PDF](raporlar/Arminoks_Siber_Guvenlik_On_Degerlendirme_Raporu.pdf)** | Kanıtların sınırı, sürüm okuma adımları, koşullu CVE adayları |
| **[SWOT analizi — PDF](raporlar/Arminoks_Sut_Otomati_SWOT_Analizi.pdf)** | Güçlü yönler, bilgi eksikleri, fırsatlar, koşullu tehditler |

**Sonuç:** Otomatta kurulu yazılım sürümleri doğrulanamadı. Doğrulanmış cihaz zafiyeti yok; ilgili olabilecek CVE kayıtları koşullu adaydır. Gerçek cihaz testi yapılmadı.

## Makine

**Arminoks süt otomatı** — AISI 304 kabin, 0–4 °C soğutma, programlanabilir karıştırıcı, kendinden emişli dolum pompası, dokunmatik panel, USB satış geçmişi, her dolumdan sonra otomatik yıkama, opsiyonel SMS modülü ve ödeme seçenekleri. Atama no 35 (SAMİB).

Özellikler, kabuller ve kaynaklar: **[Makine profili](labs/00-makine-profili.md)** · [PDF](pdf/00-makine-profili.pdf)

## Föyler

| Hafta | Laboratuvar | Çıktı | Evidence Pack | Ek soru | Föy |
|---|---|---|---|---|---|
| 0 | Makine Profili | Sistem sınırı, varsayımlar | Tümü | — | [Markdown](labs/00-makine-profili.md) · [PDF](pdf/00-makine-profili.pdf) |
| 1 | Lab 1 · Safety Architecture | Safety Function Map | EP 03 | 4 | [Markdown](labs/lab1-safety-architecture.md) · [PDF](pdf/lab1-safety-architecture.pdf) |
| 2 | Lab 2 · IEC 62443 Mini Workshop | Zone / Conduit Diagram | EP 01 · EP 05 | 4 | [Markdown](labs/lab2-iec62443-zone-conduit.md) · [PDF](pdf/lab2-iec62443-zone-conduit.pdf) |
| 3 | Lab 3 · Threat & Risk + Risk Matrix | Risk Register | EP 04 | 4 + 5 ders notu | [Markdown](labs/lab3-threat-risk-matrix.md) · [PDF](pdf/lab3-threat-risk-matrix.pdf) |
| 4 | Lab 4 · Secure Remote Access | Secure Architecture | EP 02 · EP 06 | 4 | [Markdown](labs/lab4-secure-remote-access.md) · [PDF](pdf/lab4-secure-remote-access.pdf) |
| 5 | Lab 5 · SBOM / CVE / Patch | Vulnerability Decision | EP 09 · EP 10 · EP 11 | 4 | [Markdown](labs/lab5-sbom-cve-patch.md) · [PDF](pdf/lab5-sbom-cve-patch.pdf) |
| 6 | Lab 6 · CRA Incident Simulation | Incident Workflow | EP 13 | 4 | [Markdown](labs/lab6-cra-incident-simulation.md) · [PDF](pdf/lab6-cra-incident-simulation.pdf) |
| 7 | Lab 7 · AI Safety Challenge | AI Fail-Safe Decision | EP 03 · EP 15 | 4 | [Markdown](labs/lab7-ai-safety-challenge.md) · [PDF](pdf/lab7-ai-safety-challenge.pdf) |

Tüm föyler tek dosyada, yer imli: **[pdf/00-tum-foyler.pdf](pdf/00-tum-foyler.pdf)**. Genel föyde LAB8 bulunmadığı için kapsam dışıdır.

## Föylerdeki işaretler

| İşaret | Anlamı |
|---|---|
| `EK SORU` | Makineye özgü, kendi eklediğimiz soru |
| `UYARLANDI` | Föyün genel örneği bu makineye göre değiştirildi (ör. LAB7 robot → dolum pompası) |
| `DERS NOTU` | LAB3 ders notundaki tartışma sorusu |
| D01–D08 · V01–V10 · H01–H07 | Üretici bilgisi · ders kabulü · koruma gereksinimi |
| SF-01–SF-04 | Emniyet ve ürün koruma işlevleri (Lab 1) |
| Z0–Z5 · C01–C07 · G01–G05 | Bölgeler, geçişler ve giriş kapıları (Lab 2) |
| A · W · U · AK · B · F | Envanter: donanım, yazılım, hesap, anahtar, dış bağlantı, veri akışı (Lab 2) |
| R-01–R-04 | Risk Register senaryoları (Lab 3) |
| KT01–KT07 | Önerilen doğrulama testleri (Lab 4) |

## Evidence Pack durumu

| # | Başlık | Durum | Kaynak |
|---|---|---|---|
| 01 | Asset Inventory | Taslak | Lab 2 — A/W/U/K/B/F envanteri |
| 02 | Network Architecture | Taslak | Lab 4 — hedef mimari |
| 03 | Safety Functions | Taslak | Lab 1 — SF-01–SF-04 · Lab 7 — YZ emniyet zincirinin dışında |
| 04 | Risk Assessment | Taslak | Lab 3 — R-01–R-04 |
| 05 | Zone & Conduit | Taslak | Lab 2 — Z0–Z5, C01–C07 |
| 06 | Remote Access Procedure | Taslak | Lab 2 Görev B · Lab 4 süreli bakım prosedürü |
| 07 | User/Role Matrix | Taslak | Lab 4 — operatör / servis / yetkili değişiklik rolleri |
| 08 | Software/Firmware Inventory | Taslak | Lab 5 + [CVE envanteri](raporlar/Arminoks_Yazilim_Surum_CVE_Envanteri.xlsx) — kurulu sürüm okunmadı |
| 09 | SBOM | Taslak | Lab 5 — SBOM taslağı |
| 10 | Vulnerability Records | Taslak | Lab 5 — VD-01 · koşullu gerçek CVE adayları |
| 11 | Patch/Update Records | Taslak | Lab 5 — yama ve geri dönüş planı |
| 12 | Backup & Restore | Taslak | Lab 4 adım 2 · Lab 6 — bilinen iyi yedekten geri yükleme |
| 13 | Incident Response | Taslak | Lab 6 — 15 dk / 2 sa / 24 sa / 72 sa / 14 gün akışı |
| 14 | Change Management | Taslak | Lab 5 yama süreci · Lab 7 model güncellemesi |
| 15 | Verification/Test | Taslak | Lab 4 — KT01–KT07 · Lab 7 — eşik doğrulama |

Durumlar kanıt hiyerarşisini izler: **Yok → Taslak → Var → Doğrulanmış.** Hiçbir başlık saha testiyle doğrulanmadığı için "Doğrulanmış" yoktur.

## Repo yapısı

```text
├── README.md
├── labs/                 ← föylerin Markdown kaynağı (00 profil + Lab 1–7)
├── pdf/                  ← föy tasarımında PDF'ler + 00-tum-foyler.pdf
├── raporlar/             ← yazılım/CVE envanteri, teknik rapor, SWOT
└── scripts/              ← build_pdf.py + foy.css (PDF üretimi)
```

## PDF'leri yeniden üretme

Hazır PDF'leri okumak için kurulum gerekmez. Markdown'dan yeniden üretmek için:

```bash
python -m pip install -r requirements.txt
python scripts/build_pdf.py
```

Chrome veya Chromium gerekir; bulunamazsa `CHROME=/yol/chrome` ile gösterilir (Playwright'ın `chrome-headless-shell`'i otomatik bulunur). İlk çalıştırmada fontlar ve Mermaid indirilir. Script her föy sorusunun PDF'te yer aldığını, her föyde 4 ek soru olduğunu ve bağlantıların çalıştığını kendisi kontrol eder; biri eksikse hata verir. `raporlar/` bu komutla değişmez.

## Kaynaklar

- Öğretmenin `2.1. lab_foyleri_genel.pdf` föyü (LAB1–7 görevleri), `2.2 lab_foyleri_paketpro.pdf` (uyarlama örneği), `LAB3.pdf` ders notu — yeniden dağıtılmaz
- [Arminoks süt otomatı broşürü](https://www.arminoks.com/wp-content/uploads/2019/07/ARMINOKS-S%C3%9CT-OTOMATI-BRO%C5%9E%C3%9CR%C3%9C.pdf)
- [NIST SP 800-82 Rev.3 — OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
- [Regulation (EU) 2024/2847 — Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng)

---

*Bu repo bir eğitim çıktısıdır; resmî denetim, uygunluk değerlendirmesi veya belgelendirme değildir ve CE/mevzuat uygunluğu garantisi vermez. Firma ile iletişim, aktif tarama ve saha testi yapılmamıştır.*
