# Safety 4.0 | Arminoks Süt Otomatı

**Batuhan Yaşar Özkan · 230541050 · Atama sıra no: 35 · 26 Ekim 2026**

Arminoks Makina İmalatı ve Pazarlama San. Tic. Ltd. Şti. tarafından üretilen süt otomatı ürün ailesinin kamuya açık bilgilerle incelendiği **LAB 1–5 eğitim çalışması**. Atama listesindeki kuruluş grubu SAMİB'dir; grup/şube bilgisi verilmediği için ayrıca doldurulmamıştır.

## Amaç ve sınır

Normal kontrol, emniyet ve gıda güvenliği işlevlerinin siber müdahaleyle nasıl etkilenebileceğini göstermek; bunlara karşı gereksinim ve doğrulama ölçütleri hazırlamak. Bu çalışma gerçek makinede tespit edilmiş açık raporu, saha testi, sertifika veya mevzuata uygunluk beyanı değildir. Firmaya/derneğe ulaşılmamış, aktif tarama yapılmamıştır.

**D = kaynakla doğrulanan ürün ailesi bilgisi; V = eğitim varsayımı; H = hedef gereksinim/öneri.** Bir dokümanın hazırlanması, önerinin gerçek makinede uygulanmış olması anlamına gelmez.

## Okuma sırası ve teslimler

| Sıra | Belge | Çıktı | Evidence Pack |
|---|---|---|---|
| 0 | [Makine profili](docs/00-makine-profili.md) | Kaynaklar, sistem sınırı, ortak varsayımlar | Destek |
| 1 | [LAB 1](docs/lab1-safety-architecture.md) | Safety Function Map; 8 föy sorusu + 4 ek soru | EP 03 |
| 2 | [LAB 2](docs/lab2-zone-conduit.md) | Envanter, zone/conduit; 3 soru, 6 karar, PaketPro varyantı + 4 ek soru | EP 01 / EP 05 |
| 3 | [LAB 3](docs/lab3-risk-register.md) | 4 profilli, gerekçeli Risk Register; 2 föy + 5 tartışma + 4 ek soru | EP 04 |
| 4 | [LAB 4](docs/lab4-secure-remote-access.md) | Başlangıç/hedef mimari; Görev A/B + 4 ek soru | EP 02 / EP 06 |
| 5 | [LAB 5](docs/lab5-vulnerability-decision.md) | 5 föy sorusu, SBOM taslağı, yama karar akışı + 4 ek soru | EP 09 / EP 10 / EP 11 |
| 6 | [SWOT ve doğrulama planı](docs/06-swot-dogrulama.md) | Riskler, önlemler ve kabul testleri | Destek / EP 15 taslağı |
| 7 | [Gereksinim eşleştirmesi](docs/07-teslim-kontrolu.md) | Föy sorusu → yanıt → kontrol | Teslim kontrolü |

**PDF:** [Birleşik rapor](pdf/Arminoks_Sut_Otomati_LAB1-5_Rapor.pdf). Bölüm PDF'leri aynı klasördedir. [Risk verileri](data/risk_register.json) ve [CSV](data/risk_register.csv) tekrar kullanılabilir. Öğretmene ait orijinal PDF'ler bu repoya dahil edilmemiştir.

## Temel sonuç

USB satış geçmişi ve opsiyonel SMS üretici broşüründe vardır. İnternet, Ethernet, uzaktan programlama, PLC/Safety PLC markası ve firmware sürümü doğrulanmamıştır. Uzak erişimli başlangıç modeli **V05** eğitim kabulüdür. SMS bildirim modülü uzaktan kontrol cihazı sayılmaz.

Öncelik, bakımda erişilebilir hareketli parçanın beklenmedik çalışmasının engellenmesidir. Sütün sıcaklık ve temizlik koşulları da ayrıca değerlendirilir. Güvenli durum her şeyin enerjisini koşulsuz kesmek değildir: dolum engellenirken güvenli soğutma korunabilir. Tam bakım izolasyonu farklı bir işlemdir.

## Üretim ve kontrol

Python 3.10+ kullanılır. Windows'ta `python`, Linux'ta gerekirse `python3` yazın.

```bash
python -m pip install -r requirements.txt
python scripts/build_report.py
python scripts/verify_delivery.py
```

Derleyici Markdown kaynaklarından PDF üretir; diyagramları kendi çizim tanımlarından yeniden oluşturur. Rapor metni tek yerde, `docs/` altında tutulur. Kontroller puan aritmetiğini, kimlik bağlantılarını, kapsamı, bağlantıları ve PDF taşmalarını denetler; fiziksel emniyeti veya gerçek cihazı doğrulamaz.

PDF üretimi için DejaVu Sans yazı tipleri gerekir. Linux'ta sistemdeki DejaVu kullanılır; diğer sistemlerde `DejaVuSans.ttf` ve `DejaVuSans-Bold.ttf` dosyalarını `fonts/` klasörüne koyun veya `ARMINOKS_FONT_DIR` değişkenini tanımlayın. Hazır PDF'leri okumak için Python veya yazı tipi kurulumu gerekmez.

## Kanıt durumu

LAB 1–5 belge teslimleri hazırlanmıştır. Evidence Pack kayıtlarının saha durumu **Taslak**tır. Gerçek BOM/SBOM, devre şeması, ölçüm, safety validation ve yama kurulumu kaydı yoktur. LAB 6–7 kapsam dışıdır. Ek soruların tamamı yanıtlanmıştır; teknik bilinmeyenler varsayım defterinde görünürdür.

## GitHub'a yerleştirme

Repo adı önerisi: `safety40-arminoks-sut-otomati`. [Yükleme adımları](GITHUB-YUKLEME.md). Lisansı bilinmeyen ders materyalleri ve üretici görselleri yeniden dağıtılmaz; yalnız kaynak bağlantıları verilir.
