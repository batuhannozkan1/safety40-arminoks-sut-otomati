# Destek | SWOT, doğrulama ve sunum özeti

Bu bölüm ek değerlendirmedir; föy sorularının yerine geçmez. Saha hakkında olumlu/olumsuz güvenlik hükmü vermez.

## SWOT: eğitim modelinin değerlendirmesi

| Boyut | Değerlendirme | Dayanak |
|---|---|---|
| Güçlü | Üretici sıcaklık, otomatik yıkama, panel ve USB özelliklerini yayımlamış | D02/D05/D07; analiz için açık başlangıç |
| Zayıf / bilgi eksikliği | Sürüm, devre, ağ, erişim ve koruma donanımı bilinmiyor | Gerçek kurulum hakkında sonuç sınırı |
| Fırsat | Satış izni, ürün uygunluğu ve bakım koruması ayrı gereksinimlere bağlanabilir | H01–H07; izlenebilir tasarım |
| Tehdit / koşullu | Bakım yazması veya program değişikliği koruma koşullarını aşabilir | V05–V08; R-01–R-04 |

## Doğrulama planı: gerçek test yapılmadı

Testler yalnız yetkili ve güvenli test düzeneğinde yapılmalıdır. Gerçek makinede müşteri varken koruma bypass edilmez. Yazılım dosyası kontrolleri bu testlerin yerine geçmez.

| Test | Gereksinim | Deneme | Tamamlanma ölçütü |
|---|---|---|---|
| D01 | H01 / SF-01 | Kapak açık, hata bilgisi ve hareket talebi kombinasyonları | Tehlikeli hareket yok; duruş/erişim süresi uzman ölçümüyle uygun |
| D02 | H02 / SF-02 | Ölçüm kaybı, geçersiz değer, geçmiş uygunsuzluk, sahte normal ekran | Satış kapalı; güvenli soğutma/uyarı sürer; ürün onayı gerekir |
| D03 | H03 / SF-03 | Enerji dönüşü, reset, haberleşme geri gelişi | Kendiliğinden hareket yok; ayrı yerel başlatma |
| D04 | H04 / SF-04 | Satış ve yıkama talebinin aynı anda verilmesi; durulama belirsizliği | Ürün ve tehlikeli temizleme yolları birlikte açılmaz |
| D05 | H05 | Yanlış ürün paketi, bozuk bütünlük, yetkisiz ayar/proje değişikliği | Reddetme, kayıt, güvenilir yedek ve destekli kurtarma kanıtı |
| D06 | H06 | Yanlış rol, MFA eksikliği, süre bitimi, koruma programlama isteği | Giriş/yazma reddi; süre sonunda erişim kesilir |
| D07 | H07 | Ağ/panel/servis bağlantısı kaybı | Koruma çalışır; satış izni kendiliğinden gelmez; soğutma güvenli davranır |

## İş planı ve tamamlanma ayrımı

1. Kaynak ve kapsam: LAB1–5 ve üretici özellikleri eşleştirildi.
2. Analiz: İşlev, giriş, risk ve gereksinimler birbirine bağlandı.
3. Teslim: Markdown, diyagramlar, PDF ve kontrol verileri üretildi.
4. Gerçek uygulama: Donanım incelemesi, güvenlik tasarımı, kurulum ve D01–D07 testleri **yapılmadı; eğitim tesliminin dışındadır**.

Nihai eğitim hedefi, eksiksiz ve dürüstçe sınırlandırılmış analizdir. Gerçek makinenin güvenli olduğunun kanıtlanması farklı bir hedef ve yetkili saha çalışması gerektirir.

## Terslikler ve önlemler

| Terslik | Önlem / B planı |
|---|---|
| Ürün broşüründeki farklı makineyi karıştırmak | K01 s.4–6 otomat bölümünü kullan; s.3 tank kapağı işlevini otomata taşıma |
| SMS'i internet/uzaktan komut sanmak | D06 ile V05'i ayrı tut |
| Bilinmeyen sürümden gerçek CVE sonucu çıkarmak | VD-01 belirsiz; gerçek SBOM/duyuru olmadan kesin karar yok |
| Güvenli duruşta soğutmayı gereksiz kesmek | İşlev bazlı güvenli durum; bakım izolasyonu ayrı |
| Küçük risk skorunda ağır yaralanmayı unutmak | S3 listesi, sorumlu ve kapanış kanıtı |
| PDF ve Markdown'ın ayrışması | Aynı Markdown'dan tekrar üretim ve dosya kontrolleri |

## Kısa sunum metni

Arminoks süt otomatını kamuya açık üretici bilgileriyle inceledim. Önce doğrulanan özellikleri varsayımlardan ayırdım. Ardından bakım hareketi, sıcaklık ve temizlik izinlerini koruma işlevlerine bağladım. Ağ modelinde altı giriş kapısı belirledim; dört farklı profil için fiziksel sonuçla biten risk senaryoları yazdım. E puanını insan maruziyeti olarak değil, yolun dışarıya açıklığı olarak kullandım. Uzak erişimde kimlik, süre ve kayıt kontrollerinin yanında koruma bağımsızlığını tanımladım. LAB5'te gerçek bileşen bilgisi bulunmadığı için temsili CVE üzerinden belirsizliği koruyan yama kararı hazırladım. Bu sonuç gerçek makinede açık bulduğum veya emniyet testi yaptığım anlamına gelmiyor.
