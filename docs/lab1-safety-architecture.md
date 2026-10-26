# LAB 1 - Safety Architecture

**Çıktı:** Safety Function Map | **EP 03** | T01/T02, PDF s.2

Şema, doğrulanmış Arminoks devresi değil, V01-V04 ve V08-V09 kabulleriyle hazırlanmış hedef koruma modelidir.

![Normal kontrol ve hedef koruma yolları](../diagrams/lab1-mimari.png)

## Föy soruları

### L1-Q1 | Bu makinede tehlike nedir? İnsan neyden zarar görür?

V02'de bakım yapan kişi karıştırıcıya erişebilir; beklenmedik çalışma el/kol yaralanmasına yol açabilir. Sıcaklık veya temizlik kontrolünün bozulması da uygun olmayan ürünün satışına ve tüketiciye biyolojik zarara uzanabilir. Bu sonuçlar analiz senaryosudur; gerçekleşmiş olay değildir.

### L1-Q2 | Safety function (emniyet fonksiyonu) hangisidir?

| ID | İşlev | Güvenli tepki | Tür |
|---|---|---|---|
| SF-01 | Karıştırıcıya erişim koruması | Erişim açıkken hareketi engelle; gerekli duruş olmadan erişim verme | Makine emniyeti hedefi |
| SF-02 | Sıcaklık ve ürün uygunluğu kontrolü | Ölçüm/ürün uygunluğu belirsizse satışı engelle | Ürün-gıda koruması |
| SF-03 | Beklenmedik yeniden başlamayı önleme | Reset veya enerji dönüşü hareket başlatmasın | Makine emniyeti hedefi |
| SF-04 | Yıkama ile satışı ayırma | Yıkama bitmeden veya durumu belirsizken satışa izin verme | Proses-gıda koruması |

SF kodları bölümler arasında bağlantı kurmak içindir; dört işlevin de sertifikalı emniyet fonksiyonu olduğu söylenmez. Broşürde E-stop ve Safety PLC bilgisi yoktur.

### L1-Q3 | Safety-related control system nerede? Şemada işaretleyin.

Şemanın kırmızı bölümü SF-01/SF-03 için önerilen emniyet yoludur: kapak/duruş bilgisi, emniyet mantığı ve hareketi engelleyen çıkış. SF-02/SF-04 ayrı ürün/proses koruma bloğunda gösterilmiştir. Normal kontrol komutu bu korumaları aşamamalıdır.

### L1-Q4 | Normal PLC ile Safety PLC farkı nedir?

Normal PLC üretim sırasını yönetir. Safety PLC, uygun tasarım ve doğrulamayla insanı koruyan işlevleri ve güvenli arıza tepkisini yürütmek için kullanılır. Ayrı cihaz veya IP adresi tek başına bağımsızlık sağlamaz; programlama yolu ve çıkışlar da incelenir.

### L1-Q5 | PLr / SIL neden var? Bu fonksiyon için neden önemli?

Bu ölçütler emniyet işlevinin gereken güvenilirliğini riskle ilişkilendirir. SF-01'in arızada da kişiyi koruyabilmesi önemlidir. Gerekli devre, kullanım ve tepki süresi bilgileri olmadığı için PLr/SIL numarası verilmez; LAB3'teki S3 de bu seviyelerin karşılığı değildir.

### L1-Q6 | Safe state (güvenli durum) nedir?

Bakım erişiminde hareket durmuş ve yeniden başlama engellenmiş olmalıdır. Ürün uygunluğu veya yıkama durumu belirsizse satış kapalı kalır; güvenli soğutma mümkünse sürer. Bakımda enerji izolasyonu ayrıca uygulanır; işletme duruşu tam izolasyon değildir.

### L1-Q7 | Safety function hangi dijital bağımlılıklara sahip?

Kapak/reset mantığı ve ayarlar SF-01/SF-03'ü; sıcaklık ölçümü ve satış izni SF-02'yi; yıkama sırası ve tamamlanma bilgisi SF-04'ü etkiler. Bu yazılım ve ayarların değiştirilmesi bakım hesabı, servis aracı veya güncelleme yoluyla mümkün olabilir kabul edilmiştir.

### L1-Q8 | Siber müdahale hangi noktadan bu fonksiyonu bozar?

Ders modelinde uzak servis ve kontrolör yazma yolu kapak/reset mantığını; yerel servis hesabı sıcaklık kararını; servis paketi de yıkama-satış sırasını etkileyebilir. LAB2'de G01-G05 yolları, LAB3'te R-01-R-04 senaryoları bu bağlantıyı açıklar.

## Ek sorular

### L1-E1 | Her şeyi kapatmak neden her zaman güvenli değildir?

Dolumu ve tehlikeli hareketi durdurmakla soğutmayı durdurmak farklı kararlardır. Satış engellenirken güvenli soğutmanın sürmesi ürünün daha fazla bozulmasını önleyebilir.

### L1-E2 | Panel normal sıcaklık gösteriyorsa satış yapılabilir mi?

Tek ekran değeri yeterli değildir. Ölçümün geçerliliği, geçmiş sapmalar ve temizliğin tamamlanması da değerlendirilmelidir; kabul eşikleri bu çalışmada uydurulmamıştır.

### L1-E3 | Reset neden başlatma olmamalı?

Reset koruma hatasının giderildiğini kabul eder. Hareket için ayrıca güvenli koşullar ve ayrı yerel başlatma gerekir; kişi içerideyken reset hareket başlatmamalıdır.

### L1-E4 | Emniyet bağımsızlığını nasıl sınarız?

Yetkili bir test düzeneğinde kapak açıkken normal kontrolöre hareket talebi verilir; hareket engellenmelidir. Ayrıca uzaktan koruma ayarı değişikliği ve enerji dönüşü denenir. Bunlar test önerisidir; bu çalışmada uygulanmamıştır.
