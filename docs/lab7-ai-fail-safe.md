# LAB 7 — Arminoks Süt Otomatı AI Fail-Safe Kararı

**Batuhan Yaşar Özkan | 230541050 | Atama 35 | 06.11.2026**

Kaynak: öğretmenin `2.1. lab_foyleri_genel.pdf` dosyası, PDF sayfa 8. Üç görev ve karar tablosu aşağıda karşılanmıştır. Çıktı: AI Fail-Safe Decision / EP 03 + EP 15.

## Ürün bilgisi ve eğitim senaryosu

Arminoks süt otomatında kamera, robot veya yapay zekâ kullanıldığına ilişkin kanıt bulunmamaktadır. Bu laboratuvarın YZ zinciri, **yalnız eğitim için önerilen** bir ek işlevdir: dolum alanındaki kabın varlığını ve konumunu kamerayla değerlendiren model doluma yardımcı bir izin önerir. Robot yerine makinenin pompalı dolum işlevi ele alınmıştır. Kamera ve model, gerçek envantere kurulu bileşen olarak eklenmemiştir.

Üreticide belgeli işlevler soğutma, karıştırma, dolum, panel, USB satış geçmişi ve otomatik yıkamadır. Bir görüntü sınıflandırması sütün mikrobiyolojik uygunluğunu, gerçek sıcaklığını veya yıkamanın yeterliliğini kanıtlamaz.

## L7-Q1 | Model yanlış sınıflandırdı ve uygunsuz kaba OK verdi. Sistem ne yapmalı?

YZ'nin OK çıkışı tek başına dolum başlatamaz. Önerilen mimaride bağımsız kap/konum doğrulaması, ürün ve sıcaklık uygunluğu, temizlik durumu ve çalışma modu izinleri ayrıca aranır. İkinci kontrol yoksa veya kararlar çelişirse dolum izni verilmez; operatör incelemesine geçilir. Fiziksel koruma, modelden ve normal kontrol yazılımından bağımsız gereksinim olarak tanımlanır; mevcut cihazda uygulandığı ileri sürülmez.

İnsan onayı, emniyet veya ürün uygunluğu kilidini aşan bir yetki değildir. Kabın doğru olduğu doğrulansa bile diğer koşullar sağlanmadan satış açılmaz. Otomatik doluma geri dönüş ayrı, yetkili ve kayıtlı bir karardır. Kullanılan kavramlar: ikinci doğrulama, fail-safe, human override.

## L7-Q2 | Kamera girdisi bozuk veya sahte. Nasıl fark edilir, ne yapılır?

Önerilen kontroller; görüntünün güncelliği ve zaman sırası, akışın donması/kesilmesi, sıra dışı tekrarlar, aydınlatma ve görüntü kalitesi ile bağımsız kap/konum bilgisinin tutarlılığıdır. Bu işaretler sahteciliğin kesin tespiti diye sunulmaz; gerçek algılama başarımı test edilmelidir. Bir kimlik/akış doğrulaması da görüntü içeriğinin doğru olduğunu tek başına kanıtlamaz.

Şüpheli girdide YZ'den dolum izni kabul edilmez, otomatik dolum bekletilir ve olay operatöre gösterilir. İzlenebiliyorsa görüntü zamanı, model sürümü, karar, ret nedeni ve bağımsız kontrol kaydı korunur. YZ arızası koruma işlevini devre dışı bırakamaz. Güvenli soğutma, tanımlı proses koşulları içinde sürdürülür. Kullanılan kavramlar: monitoring, fail-safe, fallback.

## L7-Q3 | Modelin confidence değeri düştü. Eşik ne olmalı, altında ne yapılır?

Gerçek kamera/model, doğrulama verisi ve kabul edilen hata sınırı bulunmadığından 0,90 veya 0,95 gibi bir eşik atanamaz. Modelin confidence değeri, emniyet güvenilirliği veya doğrulanmış hata olasılığı değildir. Eşik; boş, yanlış, eğik ve uygun kap örnekleri, aydınlatma değişimleri ve bozuk görüntülerle temsilî, bağımsız doğrulama verisinde belirlenmeli; yanlış OK oranı ve kaçırılan durumlar için kabul ölçütüyle gerekçelendirilmelidir. Model/veri değişince yeniden değerlendirilir.

Eşik belirlenip doğrulanana kadar YZ tabanlı otomatik dolum izni devreye alınmaz. Eşik altında veya dağılım dışı girdide karar “belirsiz” kabul edilir; dolum engellenir, operatör incelemesi istenir. Doğrulanmış bağımsız manuel süreç varsa o süreç kullanılabilir; yoksa satış bekletilir. İnsan onayı temel koruma koşullarını iptal etmez. Kullanılan kavramlar: confidence threshold, fallback, human override.

## AI Fail-Safe Decision — karar tablosu

| Başarısızlık | Önerilen güvenli davranış | Kapanış için gereken kanıt |
|---|---|---|
| Model yanlış sınıflandırdı | Tek başına OK yeterli değil; bağımsız doğrulama yoksa dolum yok, operatör incelemesi | Yanlış OK örneklerinde izinsiz dolumun engellendiği izole test kaydı |
| Girdi manipüle edildi | Şüpheli/eski/tutarsız akıştan izin kabul edilmez; dolum bekler, olay kaydedilir | Donmuş, tekrar ve tutarsız görüntüler için testler; algılama sınırları |
| Confidence düştü | Doğrulanmış eşik altında belirsiz karar; dolum yok, yetkili inceleme veya doğrulanmış manuel süreç | Veri seti, model sürümü, seçilen eşik, hata ölçümleri ve kabul onayı |

## Sınır ve sonuç

YZ yardımcı karar üretir; güvenli duruma geçiş ve temel koruma koşulları YZ sonucuna bağlı bırakılmaz. Bu gereksinim taslağıdır. Model geliştirilmemiş, confidence ölçülmemiş ve gerçek makinede test yapılmamıştır. Saha incelemesi olmadan PLr/SIL atanmaz veya güvenli olduğu beyan edilmez.

## Kaynaklar

- Öğretmen genel föyü, PDF s.8: üç başarısızlık, karar tablosu ve Prediction ≠ Safety kavramı. Orijinal dosya yeniden dağıtılmamıştır.
- [Arminoks süt otomatı broşürü](https://www.arminoks.com/wp-content/uploads/2019/07/ARMINOKS-S%C3%9CT-OTOMATI-BRO%C5%9E%C3%9CR%C3%9C.pdf): gerçek ürün işlevlerinin sınırı.
- [Güncel yazılım ve CVE raporu](../raporlar/Arminoks_Siber_Guvenlik_On_Degerlendirme_Raporu.pdf): kurulu model/sürüm ve doğrulama sınırları.
