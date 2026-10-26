# Makine profili, kaynaklar ve varsayımlar

**Batuhan Yaşar Özkan | 230541050 | Arminoks Süt Otomatı (SAMİB) | 26.10.2026**

## Çalışmanın sınırı

Bu çalışma süt otomatı ürün ailesini kamuya açık bilgilerle inceler. Belirli bir seri numarasının kontrolörü, yazılımı ve ağ yapısı bilinmemektedir. Fiziksel inceleme, tarama veya test yapılmamıştır. Föy soruları bu sınır gözetilerek yanıtlanmıştır.

Bilgi türleri bütün bölümlerde aynıdır: **D** üretici kaynağındaki özellik, **V** ders senaryosu için kabul, **H** önerilen gereksinim. Öneriler uygulanmış sayılmaz.

## Üretici broşüründe belirtilen özellikler

| Kod | Özellik | Kaynak |
|---|---|---|
| D01 | AISI 304 kabin, 220 V besleme | K01, PDF s.5 |
| D02 | 0-4 °C soğutma aralığı ve panelden sıcaklık takibi | K01, PDF s.5 |
| D03 | 50/100/200/400 L seçenekleri; tanklı tipte 200/400 L | K01, PDF s.5-6 |
| D04 | Programlanabilir karıştırma ve kendinden emişli dolum pompası | K01, PDF s.5 |
| D05 | Dokunmatik panel ve satış geçmişi için USB | K01, PDF s.5 |
| D06 | SMS bilgi paylaşımı modülü opsiyonu | K01, PDF s.5 |
| D07 | Her dolumdan sonra dolum ünitesinin otomatik yıkanması | K01, PDF s.5 |
| D08 | Ödeme ve barkod seçenekleri | K01, PDF s.4-6 |

K01'in PDF s.3'ündeki ayrı dolum makinesi ve soğutma tankı bu otomata ait kabul edilmemiştir. Özellikle oradaki kapak açılınca durma özelliği süt otomatına aktarılmamıştır. Broşürün 0-4 °C değeri ürün özelliğidir; tek başına gıdanın uygunluğunu belirleyen sıcaklık-süre ölçütü değildir.

## Çalışma modeli

Süt muhafaza edilir, soğutulur ve karıştırılır; satış talebinde dolum yapılır. Dolumdan sonra yıkama sırası çalışır. Analiz; panel, kontrolör, karıştırıcı, pompa, soğutma, yıkama, USB ve bakım yollarını kapsar. Robot, yapay zekâ, SCADA, pastörizasyon veya bulut hizmeti eklenmemiştir.

## Ders senaryosunda kullanılan kabuller

| Kod | Kabul | Geçerli değilse etkisi |
|---|---|---|
| V01 | Panelin bağlı olduğu programlanabilir kontrolör vardır; marka/sürüm bilinmez | Gerçek kontrol yapısına göre model güncellenir |
| V02 | Bakım sırasında karıştırıcıya erişilebilir | Erişim yoksa R-01/R-04 yaralanma zinciri yeniden değerlendirilir |
| V03 | Yıkama ve satış aynı dolum bölümünde farklı çalışma durumlarıdır | Temizlik-satış ilişkisi gerçek akışa göre değiştirilir |
| V04 | Sıcaklık ölçümü ve satış izni yazılımda değerlendirilir | Bağımsız kontrol varsa R-02 zincirine eklenir |
| V05 | LAB2-4 için bir bakım bilgisayarı ve sürekli açık uzak servis yolu kabul edilir | Uzak erişim yoksa bu yol temel kurulumdan çıkarılır |
| V06 | V05 yolunda değiştirilmemiş varsayılan kimlik bilgisi ve geniş yazma yetkisi kabul edilir | Kimlik ve erişim önlemlerine göre L/E yeniden puanlanır |
| V07 | Yerel servis hesabı paylaşılır; ders senaryosunda USB'den servis paketi yüklenebilir | Salt veri dışa aktarımı varsa R-03'ün USB yükleme zinciri geçersiz olur |
| V08 | Başlangıçta kapak/yeniden başlama denetimi normal kontrol yazılımına bağlıdır | Bağımsız koruma varsa R-01/R-04 zinciri değişir |
| V09 | Yıkama tamamlanma bilgisi satış iznini etkileyen bir kontrol koşuludur | Gerçek yöntem farklıysa SF-04 ve R-03 güncellenir |
| V10 | LAB5'in Component X v2.4 kaydı temsili eğitim girdisidir | Gerçek varlık ve duyuru bulunduğunda ayrı kayıt gerekir |

V05-V08, üreticide bulunmuş zafiyetler değildir. SMS bildirimi internetten programlama kanıtı sayılmaz. USB'nin satış kaydı özelliği de program yüklemeyi kanıtlamaz. Kimyasal veya sıcak yıkama kullanıldığı kabul edilmemiştir. Ayrı Safety PLC kurulu olduğu söylenmez; gereken koruma LAB4'te tanımlanır.

## Kaynaklar

| ID | Kaynak | Kullanım |
|---|---|---|
| T01 | Öğretmenin `2.1. lab_foyleri_genel.pdf`, 8 PDF sayfası | PDF s.2-6: LAB1-5 soruları |
| T02 | Öğretmenin `2.2 lab_foyleri_paketpro.pdf`, 8 PDF sayfası | PDF s.2-6: makineye uyarlama örneği |
| T03 | Öğretmenin `LAB3.pdf`, 40 PDF sayfası | Slayt 23-33: ölçek; slayt 43: görev; slayt 46: tartışma |
| K01 | [Arminoks süt otomatı broşürü](https://www.arminoks.com/wp-content/uploads/2019/07/ARMINOKS-S%C3%9CT-OTOMATI-BRO%C5%9E%C3%9CR%C3%9C.pdf) | PDF s.4-6: süt otomatı özellikleri |
| K02 | [NIST SP 800-82 Rev.3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | OT güvenliği için genel rehber |

T03'ün slayt numaraları 33'ten 42'ye geçer; dosya 40 PDF sayfasıdır. Slayt 43 PDF s.35'e, slayt 46 PDF s.38'e karşılık gelir. Kaynak kontrol tarihi 26.10.2026'dır. PLr/SIL veya standartlara uygunluk seviyesi belirlemek için gerekli saha ve devre bilgileri bulunmadığından bu seviyeler atanmamıştır.
