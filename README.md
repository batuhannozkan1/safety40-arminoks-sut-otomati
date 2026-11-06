# Safety 4.0 Bootcamp — Arminoks Süt Otomatı

Safety 4.0 Readiness Bootcamp laboratuvar föylerinin **Arminoks süt otomatına** uyarlanmış, uçtan uca işlenmiş hâli: 7 laboratuvar föyü + makineye özel bir **siber güvenlik / CVE değerlendirmesi**. Bütün çalışma yalnızca kamuya açık kaynaklarla (OSINT), savunma amaçlı ve dürüst bir kanıt hiyerarşisiyle yürütüldü — doğrulanmamış hiçbir şey "doğrulandı" diye sunulmadı.

![IEC 62443-3-3](https://img.shields.io/badge/IEC_62443--3--3-kapsam-1f3864)
![CRA 2024/2847](https://img.shields.io/badge/CRA_(EU)_2024%2F2847-kapsam-1f3864)
![NIST SP 800-82r3](https://img.shields.io/badge/NIST_SP_800--82r3-rehber-1f3864)
![Yontem OSINT](https://img.shields.io/badge/Yontem-OSINT-555)
![CVE dogrulama](https://img.shields.io/badge/CVE_dogrulama-CVE_Program_+_OpenCVE-2e7d32)
![Durum](https://img.shields.io/badge/Durum-Egitim_ciktisi-999)

| Ad Soyad | Öğrenci No | Grup | Atama | Tarih |
|---|---|---|---|---|
| Batuhan Yaşar Özkan | 230541050 | Gündüz-B | 35 (SAMİB) | 06.11.2026 |

> **Değerlendirici buradan başlasın:** [Üç rapor](#üç-rapor) → [CVE bulguları](#cve-bulguları) → [Föyler](#föyler) → [Evidence Pack durumu](#evidence-pack-durumu). Yöntem ve sınırlar [en altta](#yöntem-ve-sınırlar).

---

## Üç rapor

Projenin güvenlik çıktısı üç belgede toplanır. Her biri tek tek incelenebilir; özet bulgular aşağıdaki [CVE bulguları](#cve-bulguları) bölümündedir.

| Belge | İçerik |
|---|---|
| **[Siber güvenlik değerlendirme raporu — PDF](raporlar/Arminoks_Siber_Guvenlik_On_Degerlendirme_Raporu.pdf)** | Kanıtların sınırı, sürüm okuma adımları, koşullu CVE adayları, gerekçeli elemeler |
| **[SWOT analizi — PDF](raporlar/Arminoks_Sut_Otomati_SWOT_Analizi.pdf)** | Güçlü yönler, bilgi eksikleri, fırsatlar, koşullu tehditler |
| **[Yazılım, sürüm ve CVE envanteri — Excel](raporlar/Arminoks_Yazilim_Surum_CVE_Envanteri.xlsx)** | Bileşen envanteri, kurulu sürüm durumu, etkilenen sürüm koşulları, kaynaklar |

**İki kaynaklı doğrulama.** Her CVE iki bağımsız kaynaktan teyit edildi: birincil olarak **CVE Program (cvelistV5)** CNA kaydı; ikincil çapraz-doğrulama olarak **OpenCVE Bilgi Tabanı (opencve-kb)** — CNA + NVD + EUVD + EPSS katmanlarını birleştirir. İki kaynak çeliştiğinde CNA esas alınır, fark not düşülür.

---

## CVE bulguları

> **Ana sonuç — Otomatta doğrulanmış kurulu açık: 0.** Hiçbir bileşenin marka/model/firmware/sürümü kamuya açık kaynakta doğrulanamadığı için, aşağıdaki kayıtların tamamı **koşullu adaydır**: ilgili ürün ve sürüm cihazda doğrulanırsa incelenir. Bu bir olasılık ya da test sonucu değildir.

**Geçerli koşullu aday havuzu — 9 CVE:**

| CVE | Ürün / koşul | CVSS (CNA) | Danışma kaydı |
|---|---|---|---|
| CVE-2023-22807 | LS Electric XBC-DN32U · OS 01.80 | 9.8 | ICSA-23-040-02 |
| CVE-2023-22804 | LS Electric XBC-DN32U · OS 01.80 | 9.1 | ICSA-23-040-02 |
| CVE-2023-0102 | LS Electric XBC-DN32U · OS 01.80 | 9.1 | ICSA-23-040-02 |
| CVE-2023-22806 | LS Electric XBC-DN32U · OS 01.80 | 7.5 | ICSA-23-040-02 |
| CVE-2023-22803 | LS Electric XBC-DN32U · OS 01.80 | 7.5 | ICSA-23-040-02 |
| CVE-2023-0103 | LS Electric XBC-DN32U · OS 01.80 | 7.5 | ICSA-23-040-02 |
| CVE-2023-22805 | LS Electric XBC-DN32U · OS 01.80 | 6.5 | ICSA-23-040-02 |
| CVE-2022-2758 | LS Electric XG5000 < V4.0 + PLC aileleri | 6.5 | ICSA-22-228-02 |
| CVE-2018-0842 | Windows Embedded CE 6.0 | 7.0 (NVD) | Microsoft KB4095432 |

**Gerekçeyle elenenler.** CVE-2025-49848 / 49849 / 49850 (ICSA-25-168-02) LS Electric **GMWin 4 v4.18**'e aittir; bu araç XGT/XP ailesinden ayrı ürün hattıdır (GLOFA-GM) ve otomat adaylarında izi yoktur — XP-Builder'a atfedilemez. CVE-2007-0305 tarama sırasında bir metin alt dizisiyle yanlış eşleşti; LS Electric ürünü değildir. Ayrıntı ve tam gerekçeler [değerlendirme raporundadır](raporlar/Arminoks_Siber_Guvenlik_On_Degerlendirme_Raporu.pdf).

---

## Makine

**Arminoks süt otomatı** — AISI 304 kabin, 0–4 °C soğutma, programlanabilir karıştırıcı, kendinden emişli dolum pompası, dokunmatik panel, USB satış geçmişi, her dolumdan sonra otomatik yıkama, opsiyonel SMS modülü ve ödeme seçenekleri.

Özellikler, kabuller ve kaynaklar: **[Makine profili](labs/00-makine-profili.md)** · [PDF](pdf/00-makine-profili.pdf)

---

## Föyler

Her föy, öğretmenin genel föyündeki görevleri **aynı sırayla ve aynı soru metniyle** yanıtlar; sonuna makineye özgü 4 ek soru ekler. Föyler hem **Markdown** (GitHub'da okunur) hem **PDF** (föy tasarımında, yazdırılabilir) olarak bulunur.

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

### Föylerdeki işaretler

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

---

## Evidence Pack durumu

Durumlar kanıt hiyerarşisini izler: **Yok → Taslak → Var → Doğrulanmış.** Hiçbir başlık saha testiyle doğrulanmadığı için "Doğrulanmış" yoktur — bu, çalışmanın dürüstlük sınırıdır.

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
| 10 | Vulnerability Records | Taslak | Lab 5 · [9 koşullu CVE adayı](#cve-bulguları) |
| 11 | Patch/Update Records | Taslak | Lab 5 — yama ve geri dönüş planı |
| 12 | Backup & Restore | Taslak | Lab 4 adım 2 · Lab 6 — bilinen iyi yedekten geri yükleme |
| 13 | Incident Response | Taslak | Lab 6 — 15 dk / 2 sa / 24 sa / 72 sa / 14 gün akışı |
| 14 | Change Management | Taslak | Lab 5 yama süreci · Lab 7 model güncellemesi |
| 15 | Verification/Test | Taslak | Lab 4 — KT01–KT07 · Lab 7 — eşik doğrulama |

---

## Yöntem ve sınırlar

- **Yalnızca kamuya açık kaynak (OSINT).** Üretici broşür/katalogları, teknik kılavuzlar, ürün görselleri ve resmî zafiyet kayıtları. Gerçek cihaza bağlanılmadı; ağ/aktif tarama ve zafiyet sömürüsü yapılmadı.
- **İki kaynaklı CVE doğrulama.** Birincil: CVE Program (cvelistV5) CNA kaydı. İkincil: OpenCVE Bilgi Tabanı (CNA + NVD + EUVD + EPSS). Çelişkide CNA esas alınır.
- **Bileşen kimliği doğrulanamadı.** Panel/HMI, PLC, ödeme/SMS/yazıcı/sıcaklık modüllerinin marka-model-firmware'i kamuya açık kaynakta yoktur; LS Electric adaylığı yalnızca fotoğraftaki logoya dayanır (güven düzeyi düşük).
- **Kaynak bütünlüğü.** SATSO'daki katalog dosyasının, üreticinin kendi 2023 kataloğuyla MD5 olarak birebir aynı olduğu doğrulandı; bağımsız kaynak sayılmadı.

## Repo yapısı

```text
├── README.md
├── labs/                 ← föylerin Markdown kaynağı (00 profil + Lab 1–7)
├── pdf/                  ← föy tasarımında PDF'ler + 00-tum-foyler.pdf
├── raporlar/             ← siber güvenlik raporu, SWOT, yazılım/CVE envanteri
└── scripts/              ← build_pdf.py + foy.css (PDF üretimi)
```

## PDF'leri yeniden üretme

Hazır PDF'leri okumak için kurulum gerekmez. Markdown'dan yeniden üretmek için:

```bash
python -m pip install -r requirements.txt
python scripts/build_pdf.py
```

Chrome veya Chromium gerekir; bulunamazsa `CHROME=/yol/chrome` ile gösterilir (Playwright'ın `chrome-headless-shell`'i otomatik bulunur). İlk çalıştırmada fontlar ve Mermaid indirilir. Script her föy sorusunun PDF'te yer aldığını, her föyde 4 ek soru olduğunu ve bağlantıların çalıştığını kendisi kontrol eder; biri eksikse hata verir. `raporlar/` bu komutla değişmez.

## Standartlar ve kaynaklar

- Öğretmenin `2.1. lab_foyleri_genel.pdf` föyü (LAB1–7 görevleri), `2.2 lab_foyleri_paketpro.pdf` (uyarlama örneği), `LAB3.pdf` ders notu — yeniden dağıtılmaz
- [Arminoks süt otomatı broşürü](https://www.arminoks.com/wp-content/uploads/2019/07/ARMINOKS-S%C3%9CT-OTOMATI-BRO%C5%9E%C3%9CR%C3%9C.pdf)
- [IEC 62443-3-3 — System security requirements and security levels](https://webstore.iec.ch/publication/7033)
- [NIST SP 800-82 Rev.3 — Guide to OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
- [Regulation (EU) 2024/2847 — Cyber Resilience Act](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng)
- Zafiyet kayıtları: [CVE Program (cvelistV5)](https://github.com/CVEProject/cvelistV5) · [OpenCVE Bilgi Tabanı](https://github.com/opencve/opencve-kb) · [CISA ICS Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories)

---

*Bu repo bir eğitim çıktısıdır; resmî denetim, uygunluk değerlendirmesi veya belgelendirme değildir ve CE/mevzuat uygunluğu garantisi vermez. Firma ile iletişim, aktif tarama ve saha testi yapılmamıştır.*
