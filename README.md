# Safety 4.0 - Arminoks Süt Otomatı

**Batuhan Yaşar Özkan | 230541050 | Atama no: 35 | 26 Ekim 2026**

Arminoks Makina İmalatı ve Pazarlama San. Tic. Ltd. Şti. süt otomatı için hazırlanmış LAB 1-5 çalışmasıdır. Atama listesindeki kuruluş grubu SAMİB'dir.

## Kapsam ve yöntem

Üreticinin açık broşüründeki bilgiler kullanılmıştır. Firmayla iletişim kurulmamış ve makine üzerinde test yapılmamıştır. Kontrol sistemi hakkında bilinmeyen ayrıntılar, ders sorularını yanıtlamak için açıkça varsayım olarak belirtilmiştir.

**D:** üretici kaynağında belirtilen özellik. **V:** eğitim senaryosu için kabul. **H:** önerilen koruma gereksinimi. Bu analiz, gerçek makinede açık bulunduğu veya emniyet doğrulandığı anlamına gelmez.

## Bölümler

| Bölüm | İçerik | Çıktı |
|---|---|---|
| [Makine profili](docs/00-makine-profili.md) | Ürün bilgileri, kaynaklar ve varsayımlar | Sistem sınırı |
| [LAB 1](docs/lab1-safety-architecture.md) | 8 föy sorusu ve 4 ek soru | Safety Function Map |
| [LAB 2](docs/lab2-zone-conduit.md) | Envanter, bölgeler, geçişler ve 6 erişim kararı | Zone / Conduit Diagram |
| [LAB 3](docs/lab3-risk-register.md) | 4 senaryo, puanlar, önlemler ve tartışma soruları | Risk Register |
| [LAB 4](docs/lab4-secure-remote-access.md) | Başlangıç/hedef mimari ve bağımsızlık gereksinimleri | Secure Architecture |
| [LAB 5](docs/lab5-vulnerability-decision.md) | 5 föy sorusu, bileşen inceleme ve yama kararı | Vulnerability Decision |
| [SWOT ve doğrulama planı](docs/06-swot-dogrulama.md) | Değerlendirme ve önerilen testler | Destekleyici çalışma |
| [Teslim kontrolü](docs/07-teslim-kontrolu.md) | Soru ve yanıt eşleştirmesi | Kapsam listesi |

**[Birleşik PDF raporu](pdf/Arminoks_Sut_Otomati_LAB1-5_Rapor.pdf)** ve bölüm PDF'leri `pdf/` klasöründedir. Risk kayıtları [JSON](data/risk_register.json) ve [CSV](data/risk_register.csv) biçiminde de bulunur. Her laboratuvarda 4, toplam 20 ek soru yanıtlanmıştır. LAB 6-7 kapsam dışındadır.

## Dosyaları yeniden üretme

Hazır PDF'leri okumak için kurulum gerekmez. Kaynaklardan yeniden üretmek için Python 3.10+ kullanılır:

```bash
python -m pip install -r requirements.txt
python scripts/build_report.py
python scripts/verify_delivery.py
```

PDF üretimi için DejaVu Sans gerekir. Linux'ta sistem yazı tipleri kullanılır. Diğer sistemlerde `DejaVuSans.ttf` ve `DejaVuSans-Bold.ttf` dosyalarını `fonts/` klasörüne koyun veya `ARMINOKS_FONT_DIR` ile konumunu belirtin.

Üretim aracı raporu, risk tablolarını ve soru listesini aynı Markdown kaynaklarından günceller. Kontrol aracı kapsamı, bağlantıları, puanları, veri tutarlılığını ve PDF metin sınırlarını denetler. Sonuç [kontrol kaydındadır](data/verification.json). Bunlar belge kontrolleridir; gerçek cihaz testi değildir.

## Kaynaklar

Ana görev kaynağı öğretmenin genel föyü; uyarlama örneği PaketPro föyü; risk ölçeği kaynağı LAB3 ders notudur. Üretici ve teknik rehber bağlantıları [makine profilinde](docs/00-makine-profili.md) verilmiştir. Öğretmenin orijinal PDF'leri ve üretici görselleri repoda yeniden dağıtılmaz.
