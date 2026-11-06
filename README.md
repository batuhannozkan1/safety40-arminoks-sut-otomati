# Arminoks Süt Otomatı — Safety 4.0

**Batuhan Yaşar Özkan · 230541050 · Atama 35 · SAMİB**

Arminoks süt otomatının kamuya açık bilgilerle yapılan güvenlik incelemesi ve laboratuvar çalışmaları.

## Önce bu üç dosyayı inceleyin

| Dosya | İçerik |
|---|---|
| **[Yazılım, sürüm ve CVE envanteri — Excel](raporlar/Arminoks_Yazilim_Surum_CVE_Envanteri.xlsx)** | Yazılım referansları, kurulu sürüm durumu, etkilenen sürüm koşulları ve kanıt belgeleri |
| **[Teknik değerlendirme raporu — PDF](raporlar/Arminoks_Siber_Guvenlik_On_Degerlendirme_Raporu.pdf)** | Kanıtların sınırı, sürüm okuma adımları ve koşullu CVE adayları |
| **[SWOT analizi — ayrı PDF](raporlar/Arminoks_Sut_Otomati_SWOT_Analizi.pdf)** | Güçlü yönler, bilgi eksikleri, fırsatlar ve koşullu tehditler |

**Mevcut sonuç:** Otomatta kurulu yazılım sürümleri doğrulanamadı. Doğrulanmış cihaz zafiyeti yok; ilgili olabilecek CVE kayıtları koşullu adaydır. Gerçek cihaz testi yapılmadı. Üreticinin yayımladığı paket sürümü, otomatta kurulu sürüm değildir.

## Laboratuvarlar

| Ödev | Çalışma | Durum |
|---|---|---|
| LAB1 | [Safety Architecture](docs/lab1-safety-architecture.md) | Eğitim analizi |
| LAB2 | [Zone / Conduit](docs/lab2-zone-conduit.md) | Eğitim analizi |
| LAB3 | [Risk Register](docs/lab3-risk-register.md) | Gerekçeli eğitim senaryoları |
| LAB4 | [Secure Remote Access](docs/lab4-secure-remote-access.md) | Varsayımlar ve hedef gereksinimler |
| LAB5 | [SBOM / CVE / Patch](docs/lab5-vulnerability-decision.md) | Föy yanıtları; gerçek CVE adayları yukarıdaki raporlarda |
| LAB6 | [Incident Workflow](docs/lab6-incident-workflow.md) · [PDF](pdf/LAB6_Incident_Workflow.pdf) | Özgün föyün 5 görevi süt otomatına uyarlandı |
| LAB7 | [AI Fail-Safe Decision](docs/lab7-ai-fail-safe.md) · [PDF](pdf/LAB7_AI_Fail_Safe.pdf) | Özgün föyün 3 görevi ve karar tablosu uyarlandı |
| LAB8 | Özgün yönerge bekleniyor | Genel föyde LAB8 yok; içerik tahmin edilmedi |

LAB6'daki olay ve LAB7'deki kamera/YZ işlevi eğitim senaryosudur. Gerçek olay, kurulu YZ sistemi veya doğrulanmış kontrol olarak sunulmaz. CRA'nın zafiyet ve ciddi olay bildirim süreleri LAB6'da ayrı açıklanmıştır.

## Kaynak ve doğrulama

[Makine profili](docs/00-makine-profili.md) · [Teslim kapsamı](docs/07-teslim-kontrolu.md) · [Önerilen doğrulamalar](docs/06-swot-dogrulama.md)

Özgün genel föyün PDF s.7'si LAB6, s.8'i LAB7 içindir. Öğretmenin dosyaları ve üretici görselleri yeniden dağıtılmaz. Firma ile iletişim, aktif tarama ve saha testi yapılmamıştır. Ürün bilgisi ile eğitim kabulleri ayrı tutulur.

Hazır dosyaları okumak için kurulum gerekmez. Laboratuvar PDF'lerini kaynaklardan üretmek ve belge kontrollerini çalıştırmak için:

```bash
python -m pip install -r requirements.txt
python scripts/build_report.py
python scripts/verify_delivery.py
```

PDF üretimi DejaVu Sans gerektirir; sistemde yoksa ARMINOKS_FONT_DIR ile konumu belirtilir. Bu komutlar laboratuvar kaynaklarını ve yardımcı verileri işler. `raporlar/` altındaki üç araştırma dosyası ayrı hazırlanmış teslimlerdir; bu komutlarla üzerine yazılmaz. Kontroller belge bütünlüğünü gösterir, makine emniyetini veya öğretmenin kabulünü kanıtlamaz.
