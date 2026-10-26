# 00 | Makine profili ve ortak kabuller

Batuhan Yaşar Özkan · 230541050 · Arminoks Süt Otomatı (SAMİB) · 26.10.2026

## Amaç, yöntem ve nihai teslim

Çalışma, üreticiye başvurmadan açık kaynak üzerinden yapılan kör analizdir. İstenen sonuç, LAB 1–5 sorularının aynı makine modeliyle yanıtlandığı, kaynak/varsayım ayrımı yapılmış bir Machine Starter Pack'tir. Makineye erişim, keşif taraması, parola denemesi veya fiziksel müdahale yapılmaz. Gerçek kurulum hakkında emniyet veya zafiyet hükmü verilmez.

Bilgi etiketleri bütün bölümlerde aynıdır: **D** doğrulanmış ürün ailesi özelliği; **V** analiz varsayımı; **H** hedef öneri. D etiketi, özelliğin belirli bir seri numarasında kurulu veya güvenilir olduğu anlamına gelmez.

## Doğrulanan ürün ailesi bilgileri

Aşağıdaki kısa teknik özet K01'in süt otomatı bölümünden (PDF sayfa 4–6) alınmıştır. Broşürün sayfa 3'ündeki ayrı süt dolum makinesi ve soğutma tankı aynı makine kabul edilmemiştir.

| Kod | Özellik | Dayanak |
|---|---|---|
| D01 | AISI 304 kabin, 220 V besleme | K01, s.5 |
| D02 | Soğutma aralığı 0–4 °C; sıcaklığı panelden izleme | K01, s.5 |
| D03 | 50/100/200/400 L seçenekleri; tanklı tipte 200/400 L | K01, s.5–6 |
| D04 | Programlanabilir karıştırma; kendinden emişli dolum pompası | K01, s.5 |
| D05 | Dokunmatik panel, satış geçmişi için USB | K01, s.5 |
| D06 | SMS bilgi paylaşımı modülü opsiyonu | K01, s.5 |
| D07 | Dolum sonrasında dolum ünitesinin otomatik yıkanması | K01, s.5 |
| D08 | Ödeme/barkod seçenekleri | K01, s.4–6 |

Bu bilgiler ürün ailesini tanımlar. Analizde kapasiteye bağlı hesap yapılmadığından keyfî kapasite seçilmez. Broşürdeki 0–4 °C ürün özelliğidir; süre-sıcaklık açısından gıda kabul ölçütü veya mevzuat sınırı olarak kullanılmaz.

## İş akışı ve sistem sınırı

Modelde ürün tankına süt alınır; soğutulur ve karıştırılır; satış talebi ve izin koşulları sağlanınca pompalanır; dolum sonrası temizleme sırası yürütülür. Bakımda satış durdurulur ve gerekli enerjiler izole edilir. Bu akışın kontrol ayrıntıları V01–V09 kapsamındadır.

Sınır: otomatın paneli, varsayımsal kontrolörü, karıştırıcı/pompa/soğutma/temizlik çıkışları, sensörler, bakım aracı, USB ve opsiyonel SMS. Tedarikçi, işletme ağı ve internet dış sınırdır. Robot, SCADA, MES, yapay zekâ, pastörizasyon, tam tesis CIP hattı ve doğrulanmamış bulut hizmeti eklenmemiştir. Çiğ süt otomatı, pastörizatör sayılmaz.

## Ortak varsayım defteri

| Kod | Eğitim kabulü | Hangi sonuç buna bağlı? | Yanlışsa ne değişir? |
|---|---|---|---|
| V01 | Panelin bağlı olduğu programlanabilir bir kontrolör vardır; marka ve sürüm bilinmez | Bütün kontrol modeli | Ayrık kontrolör yoksa panel/entegre kontrolör olarak birleştirilir |
| V02 | Karıştırıcıya bakım/temizlik sırasında erişim mümkündür | SF-01, SF-03; R-01 ve R-04 | Erişim fiziksel olarak imkânsızsa bu yaralanma zinciri yeniden kurulur |
| V03 | Satış ve otomatik yıkama aynı dolum bölümünü kullanır; örnek tehlike analizinde temizlik maddesi/sıcak akış ihtimali ayrıca varsayılır | SF-04; R-03 | Yalnız soğuk su varsa kimyasal/yanık sonucu çıkarılır |
| V04 | Sıcaklık sensörü ve satış izni yazılıma bağlıdır | SF-02; R-02 | Bağımsız izleme varsa zincir o kontrol üzerinden tekrar incelenir |
| V05 | LAB 2–4 başlangıç senaryosunda servis için bir uzak bakım ağ geçidi ve bakım bilgisayarı bulunur; servis yolu sürekli açıktır | C01–C03, R-01 | Uzaktan erişim yoksa R-01 temel kurulumdan çıkar; yerel riskler kalır |
| V06 | V05 yolunda değiştirilmemiş varsayılan kimlik doğrulama ve kısıtsız kontrolör yazma yetkisi kabul edilir | R-01 L3/E3 | Gerçek erişim kontrolleriyle L/E yeniden puanlanır |
| V07 | Yerel servis hesabı paylaşılır; USB için kontrollü aktarım politikası yoktur | R-02 ve R-03 | Kişisel hesap ve kontrollü aktarım varsa L yeniden değerlendirilir |
| V08 | Başlangıçta koruyucu kapak/yeniden başlama denetimi normal kontrol yazılımına bağımlıdır; güncelleme kanalı yeterince doğrulanmaz | R-01/R-04 | Bağımsız donanım ve değişiklik kontrolleri varsa zincir kesilebilir |
| V09 | Yıkama başarısı ve durulama onayı için kontrol sinyalleri modellenir; gerçek sensör/valf topolojisi bilinmez | SF-04, test D04 | Kanıtsız sinyal başarı kabul edilmez; gerçek tasarımla yenilenir |
| V10 | LAB5'te Component X v2.4, CVSS 9.8 ve yama varlığı föyün temsili girdisidir | VD-01 | Gerçek bileşen/CVE bulunduğunda ayrı kayıt açılır |

Önemli ayrım: USB portunun bulunması D05; o porttan program çalıştırılabilmesi V07/V08'dir. SMS seçeneği D06; internet, 4G router, uzaktan komut alma veya servis protokolü varlığı değildir. Ayrı Safety PLC veya emniyet rölesi **kurulu varsayılmaz**; hedefte gereken işlevsel bağımsızlık tanımlanır.

## Güvenilirlik ve sınırlar

PLr/SIL, eldeki broşürden atanamaz. Duruş süresi, kapak erişim süresi, kullanım sıklığı, kaçınma olanağı, devre kategorisi ve bileşen verileri bilinmez. L×S×E dersin sadeleştirilmiş siber-fiziksel önceliklendirmesidir; ISO 13849/IEC 62061 hesabı değildir. Gıda güvenliği işlevleri de doğrudan bir PL/SIL belgesi sayılmaz.

## Kaynak kaydı

| ID | Kaynak | Kullanım / sınır |
|---|---|---|
| T01 | Öğretmenin `2.1. lab_foyleri_genel.pdf`, 8 sayfa | LAB1–5 ana soru ve çıktı yapısı; s.2–6 |
| T02 | Öğretmenin `2.2 lab_foyleri_paketpro.pdf`, 8 sayfa | Makineye uyarlama örneği; PaketPro özellikleri Arminoks'a aktarılmaz |
| T03 | Öğretmenin `LAB3.pdf`, 48 sayfa | s.23–33 ölçek/Register; s.43 görev; s.46 tartışma |
| K01 | [Arminoks süt otomatı broşürü](https://www.arminoks.com/wp-content/uploads/2019/07/ARMINOKS-S%C3%9CT-OTOMATI-BRO%C5%9E%C3%9CR%C3%9C.pdf) | Süt otomatı ürün ailesi özellikleri, özellikle s.4–6 |
| K02 | [NIST SP 800-82 Rev.3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | OT güvenliği, segmentasyon, uzak erişim ve değişiklik yönetimi için genel rehber |

Erişim tarihi: 26.10.2026. İnternet kaynakları resmî üretici ve NIST kaynaklarıdır. Öğretmen belgeleri özel olarak paylaşıldığı için açık repoda yeniden dağıtılmaz. ISO/IEC standartlarının tam metinlerine dayalı bir uygunluk denetimi yapıldığı iddia edilmez. Mevzuat kapsam/tarih analizi LAB1–5 teslimine eklenmemiştir.
