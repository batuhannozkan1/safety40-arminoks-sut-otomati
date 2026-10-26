# SWOT ve doğrulama planı

## SWOT

| Boyut | Değerlendirme |
|---|---|
| Güçlü | Panel, sıcaklık takibi ve otomatik yıkama gibi özelliklerin üretici broşüründe bulunması |
| Zayıf / bilgi eksikliği | Kontrolör, sürüm, ağ ve koruma devresinin bilinmemesi |
| Fırsat | Bakım, satış ve yıkama izinlerinin açık gereksinimlerle ayrılması |
| Tehdit / koşullu | Ders modelinde servis veya yazılım değişikliğinin koruma koşullarını aşabilmesi |

Bu tablo gerçek makineye yönelik denetim sonucu değildir; açık kaynak analizinin değerlendirmesidir.

## Önerilen doğrulamalar

Testler gerçek makinede yapılmamıştır. Yetkili bir düzenekte, insanı tehlikeye sokmadan uygulanmaları önerilir. KT kodları testleri, D kodları ise üretici bilgilerini belirtir.

| Test | Gereksinim | Kontrol ve beklenen sonuç |
|---|---|---|
| KT01 | H01 / SF-01 | Kapak açık/hatalıyken hareket talebi: tehlikeli hareket engellenir; duruş-erişim süresi doğrulanır |
| KT02 | H02 / SF-02 | Geçersiz sıcaklık ve ürün durumu: satış kapalı, uyarı ve güvenli soğutma davranışı tanımlı |
| KT03 | H03 / SF-03 | Reset, enerji ve haberleşme dönüşü: ayrı yerel başlatma olmadan hareket yok |
| KT04 | H04 / SF-04 | Yıkama sürerken veya tamamlanma belirsizken satış talebi: satış engellenir |
| KT05 | H05 | Bozuk/yanlış paket veya yetkisiz ayar: reddedilir, kayıt ve kurtarma yolu bulunur |
| KT06 | H06 | Yanlış rol, eksik MFA veya süre sonu: giriş/yazma reddedilir, geçici erişim kapanır |
| KT07 | H07 | Ağ/panel kaybı: koruma sürer; satış kendiliğinden açılmaz; soğutma güvenli davranır |

## Analizin değişeceği durumlar

Uzak erişim yoksa R-01'in bu yolu çıkarılır. USB yalnız satış verisi aktarıyorsa R-03'ün program yükleme yolu geçersizleşir. Karıştırıcıya erişim mümkün değilse mekanik senaryolar; gerçek temizlik ve ürün verileri farklıysa biyolojik senaryolar yeniden değerlendirilir.

PLr/SIL, gerçek SBOM, kurulu koruma devresi veya yapılmış yama testi bilgisi bu çalışmada üretilmemiştir. Bunlar için gerekli veri bulunmamaktadır.
