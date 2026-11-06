# LAB 6 — Arminoks Süt Otomatı Olay Müdahale Akışı

**Batuhan Yaşar Özkan | 230541050 | Atama 35 | 06.11.2026**

Kaynak: öğretmenin `2.1. lab_foyleri_genel.pdf` dosyası, PDF sayfa 7. Beş görev aşağıda aynı sırayla yanıtlanmıştır. Çıktı: Incident Workflow / EP 13. Bu belge masa başı eğitim senaryosudur; Arminoks'ta yaşanmış olay veya uygulanmış müdahale kaydı değildir.

## Makineye uyarlanan senaryo

Föyün 10:15 servis hesabı ihlali ve olası PLC konfigürasyon değişikliği senaryosu süt otomatına uygulanır. Servis hesabı, programlanabilir kontrolör ve olay kaydı bu görev için eğitim kabulüdür; gerçek kontrolör modeli, hesap yapısı ve uzak erişim kanıtlanmamıştır. USB satış kaydı ve opsiyonel SMS, program yükleme ya da uzaktan kontrol kanıtı sayılmaz.

Üretici soğutma, karıştırma, pompalı dolum ve otomatik yıkama işlevlerini belirtir. Bu nedenle olayda hem hareketli bileşenlere erişim hem de sıcaklık, yıkama ve satış izinlerinin bütünlüğü değerlendirilir. Sadece ekranın normal görünmesi güvenli devam için yeterli değildir.

## L6-Q1 | 10:15 — ilk 15 dakika: Kimi ararsınız? İlk üç eyleminiz?

Vardiya sorumlusu, işletmenin bakım/OT sorumlusu ve gıda güvenliği sorumlusuyla birlikte olay yöneticisini bilgilendirir. Bunlar önerilen rollerdir; Arminoks çalışanı veya atanmış kişi adı değildir.

1. **İnsanı ve ürünü koru:** Yeni satış/dolum iznini, tanımlı güvenli işletme prosedürüyle askıya al; bakım alanına erişimi sınırla. Hareketli parçaya müdahale gerekiyorsa yetkili bakım izolasyonu uygular. Soğutma gereksinimini değerlendirmeden bütün enerjiyi kesme; güvenli soğutmanın sürmesi mümkün değilse gıda sorumlusu ürünün korunmasını ayrıca yönetir.
2. **Olayı kaydet:** Tespit saatini, görülen uyarıyı, hesabı, makine kimliğinin bilinen kısmını ve ilk kararları kaydet. Yetkili şekilde görülebilen panel durumunu ve bağımsız sıcaklık ölçümünü koru. Saat kaynağını ve saat farkını belirt; sürüm veya seri numarası tahmin etme.
3. **Şüpheli erişimi sınırla:** Bakım/OT sorumlusu, gerçekten kullanılan servis yolunu ve şüpheli hesabı belirler; kayıtları koruyarak ilgili oturumu sonlandırır ve hesabı askıya alır. Doğrulanmamış VPN, bulut veya ağ bağlantısı varmış gibi işlem yapma. Reset, fabrika ayarına dönme ve program yükleme ilk müdahale değildir.

## L6-Q2 | İlk iki saat: Emniyet güvende mi? Hangi kanıt korunur, hangi hesap kapatılır?

Emniyetin güvende olduğu henüz söylenemez. Satış/dolum kısıtı sürdürülür; karıştırıcı ve pompa erişimi, varsa koruma devresi, sıcaklık ölçümünün güvenilirliği ve yıkama-satış ayrımı yetkili ekip tarafından kontrol edilir. Değişiklikten etkilenebilecek ürün ve satışlar gıda sorumlusunca ayrılır; bilinmeyen sıcaklık geçmişi güvenli kabul edilmez.

| Korunacak kayıt | Uygulama ve sınır |
|---|---|
| Servis hesabı ve oturum kayıtları | Varsa yetkili erişimle dışa alınır; silinmez. Hesap adı ve olayla ilişkisi doğrulanır. |
| Konfigürasyon ve proje | Yetkili, uygun yöntemle salt okunur kopya alınır; bilinen iyi kayıtla karşılaştırılır. Şüpheli sisteme araç kurmak için değiştirme yapılmaz. |
| Satış ve ürün geçmişi | USB satış geçmişi varsa orijinal korunur; zaman aralığı, işlem ve ilgili ürün kayıtları ilişkilendirilir. |
| Sıcaklık, alarm ve yıkama geçmişi | Gerçekte tutuluyorsa korunur. Kayıt yoksa yokluğu yazılır; eksik geçmiş üretilmez. |
| Kanıt teslim kaydı | Kim, neyi, ne zaman, hangi yöntemle aldı; SHA-256, kopyanın yeri, erişim ve teslim zinciri kaydedilir. Özet değer, bilginin doğruluğunu tek başına kanıtlamaz. |

İhlalle ilişkili **servis hesabı** askıya alınır; tüm hesaplar körlemesine silinmez. Ortak hesap varsa kapsamı belgelenir. Yetkili kurtarma erişimi kontrollü tutulur. Hesabı kapatma işleminin proses ve koruma üzerindeki etkisi bakım sorumlusunca değerlendirilir.

## L6-Q3 | 24 saat — erken uyarı için hangi bilgi hazır olmalı?

Olay kimliği, tespit ve öğrenme saatleri, bilinen ürün/model bilgisi, gözlenen yetkisiz erişim, muhtemel konfigürasyon etkisi, insan/ürün/işletim etkisi, satış/dolum kısıtı, korunan kanıtlar, olay sorumlusu ve bilinmeyenler hazır tutulur. Aktif istismar ile ciddi olay sınıflandırması ayrılır; henüz doğrulanmamış kök neden kesin bilgi diye yazılmaz. AB pazarı ve CRA kapsamı, sorumlu üretici ve bildirim muhatabı ayrıca değerlendirilir. Öğrenci veya vardiya sorumlusu kendiliğinden resmî bildirim göndermez.

## L6-Q4 | 72 saat — kök neden, etki ve önlemler: Kim ne yapıyor?

| Rol | 72 saatlik değerlendirmeye katkısı |
|---|---|
| Olay yöneticisi | Tek zaman çizgisi, kapsam, kararlar ve sorumlulukları toplar. |
| Bakım/OT sorumlusu | Hesap/erişim yolu, konfigürasyon farkı ve gerçek yazılım sürümlerini kanıtla belirler; geçici kısıtları sürdürür. |
| Gıda güvenliği sorumlusu | Etkilenen ürün ve satış aralığını, sıcaklık/temizlik kayıtlarını ve ürün hakkında alınan kararı belgeler. |
| Üretici ve yetkili bildirim sorumlusu | Ürün kapsamını ve gerekli resmî bildirimi değerlendirir; uygulanabiliyorsa bildirimi yürütür. Bu çalışma kapsamında firmaya ulaşılmamıştır. |

Kök neden bulunmadıysa “inceleme sürüyor” yazılır. Etki ve alınan önlemler mevcut kanıtla bildirilir; kesin kök neden bulunması 72 saatlik kaydı geciktirme gerekçesi yapılmaz. Yeniden işletmeye alma, yalnız hesap kapatıldı diye onaylanmaz.

## L6-Q5 | 14 gün — son rapor için hangi kayıtlar korunmuş olmalı?

Föyün 14 günlük eğitim kontrol noktasında ilk uyarı, oturum/hesap kayıtları, konfigürasyonun önce/sonra kopyaları, dosya özetleri ve teslim zinciri; sıcaklık, satış, yıkama ve ürün kararları; değişiklik onayları, doğrulama sonuçları, geri dönüş planı ve yeniden işletme izni korunmuş olmalıdır. Olmayan log veya yapılmamış test eklenmez. Gerçek olay olmadığı için burada doldurulmuş log, olay numarası veya başarılı test sonucu sunulmamıştır.

**CRA süre ayrımı:** Föyün “14 gün” kontrol noktası bütün olaylar için tek bir yasal süre değildir. Madde 14'e göre aktif istismar edilen zafiyette nihai rapor, düzeltici/azaltıcı önlem hazır olduktan sonra en geç 14 gün içinde; ciddi olayda ise 72 saatlik bildirimin sunulmasından itibaren bir ay içinde ele alınır. Erken uyarı 24, ana bildirim 72 saattir. Kapsam ve üretici yükümlülüğü doğrulanmadan bu süreler bu otomata otomatik atanamaz. Bildirim hükümlerinin uygulama tarihi 11.09.2026'dır.

## Olay akışı ve kapanış

**Tespit → insan/ürün güvenliği → şüpheli erişimi sınırlandırma → kanıt koruma → kapsam ve bildirim değerlendirmesi → kontrollü düzeltme → doğrulama → yetkili yeniden işletme → izleme.**

Satış/dolum ancak bilinen iyi konfigürasyon, ürün uygunluğu, ilgili koruma ve yıkama koşulları doğrulanıp yetkili rollerce kayıtlı onay verildiğinde açılır. Bu kabul ölçütüdür; uygulanmış test değildir.

## Kaynaklar

- Öğretmen genel föyü, PDF s.7: beş görev ve saat 10:15 eğitim senaryosu. Orijinal dosya yeniden dağıtılmamıştır.
- [Arminoks süt otomatı broşürü](https://www.arminoks.com/wp-content/uploads/2019/07/ARMINOKS-S%C3%9CT-OTOMATI-BRO%C5%9E%C3%9CR%C3%9C.pdf): ürün işlevleri.
- [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng): Madde 14 ve 71.
- [Avrupa Komisyonu — CRA reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting): bildirim türleri ve süreler, erişim 06.11.2026.
