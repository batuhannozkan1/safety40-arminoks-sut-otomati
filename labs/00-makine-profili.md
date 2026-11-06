<!-- foy lab="profil" kicker="Başlangıç föyü" short="Profil" title="Makine Profili" output="Sistem sınırı · kaynaklar · varsayımlar" -->
<!-- pdf:skip-start -->
# Makine Profili · Arminoks Süt Otomatı

📄 [PDF föyü](../pdf/00-makine-profili.pdf)

| Ad Soyad | Öğrenci No | Grup | Tarih |
|---|---|---|---|
| Batuhan Yaşar Özkan | 230541050 | Gündüz-B | 06.11.2026 |
<!-- pdf:skip-end -->

> **Kavram:** Bütün laboratuvarlar aynı makine üzerinde işlenir. Önce makinenin sınırı çizilir: **neyi biliyoruz** (üretici kaynağı), **neyi kabul ediyoruz** (ders senaryosu) ve **neyi istiyoruz** (gereksinim). Bu üçü karıştırılırsa analiz, gerçek makine hakkında yanlış iddiaya dönüşür.

> **Arminoks bağlamı:** Arminoks Makina İmalatı ve Pazarlama San. Tic. Ltd. Şti.'nin süt otomatı. Atama listesinde no 35, SAMİB kuruluş grubu. Bilgiler üreticinin kamuya açık broşüründen alındı. Firmayla iletişim kurulmadı; makine üzerinde tarama veya test yapılmadı.

## İşaretler

| Kod | Anlamı |
|---|---|
| **D01–D08** | Üretici kaynağında belirtilen özellik (doğrulanmış bilgi) |
| **V01–V10** | Ders senaryosu için yapılan kabul; sahada doğrulanmalı |
| **H01–H07** | Önerilen koruma gereksinimi (LAB4); uygulanmış sayılmaz |
| **LAB kodları** | SF-01–04 işlevler (LAB1) · Z0–Z5 bölge, C01–C07 geçiş, G01–G05 kapı, A/W/U/AK/B/F envanter (LAB2) · R-01–04 senaryo (LAB3) · KT01–07 test, uygulanmadı (LAB4) · VD-01 karar (LAB5) |
| **T · K** | Kaynaklar: öğretmen dosyaları ve dış kaynaklar (bu föyün sonu) |

## Üretici broşüründe belirtilen özellikler

| Kod | Özellik | Kaynak |
|---|---|---|
| D01 | AISI 304 paslanmaz kabin, 220 V besleme | K01, s.5 |
| D02 | 0–4 °C soğutma aralığı, panelden sıcaklık takibi | K01, s.5 |
| D03 | 50 / 100 / 200 / 400 L seçenekleri; tanklı tipte 200 / 400 L | K01, s.5–6 |
| D04 | Programlanabilir karıştırma, kendinden emişli dolum pompası | K01, s.5 |
| D05 | Dokunmatik panel; satış geçmişi için USB | K01, s.5 |
| D06 | SMS bilgi paylaşımı modülü (opsiyon) | K01, s.5 |
| D07 | Her dolumdan sonra dolum ünitesinin otomatik yıkanması | K01, s.5 |
| D08 | Ödeme ve barkod seçenekleri | K01, s.4–6 |

Broşürün s.3'ündeki ayrı dolum makinesi ve soğutma tankı bu otomata ait sayılmadı; oradaki "kapak açılınca durma" özelliği de otomata aktarılmadı. 0–4 °C bir ürün özelliğidir; gıdanın uygunluğunu tek başına belirleyen sıcaklık-süre ölçütü değildir.

## Çalışma modeli

Süt tankta soğutulur ve karıştırılır; satış talebinde pompa ile dolum yapılır; her dolumdan sonra yıkama sırası çalışır. Analiz panel, kontrolör, karıştırıcı, pompa, soğutma, yıkama, USB ve bakım yollarını kapsar. Ürün envanterine robot, yapay zekâ, SCADA, pastörizasyon veya bulut hizmeti **eklenmedi**. LAB7'deki kamera/YZ zinciri yalnız eğitim senaryosudur.

## Ders senaryosu kabulleri

| Kod | Kabul | Geçerli değilse |
|---|---|---|
| V01 | Panelin bağlı olduğu programlanabilir bir kontrolör var; marka/sürüm bilinmiyor | Model gerçek kontrol yapısına göre güncellenir |
| V02 | Bakım sırasında karıştırıcıya erişilebilir | R-01/R-04 yaralanma zinciri yeniden değerlendirilir |
| V03 | Yıkama ve satış aynı dolum bölümünde farklı çalışma durumlarıdır | Yıkama–satış ilişkisi gerçek akışa göre değişir |
| V04 | Sıcaklık ölçümü ve satış izni yazılımda değerlendirilir | Bağımsız kontrol varsa R-02 zincirine eklenir |
| V05 | LAB2–4 için bir bakım bilgisayarı ve sürekli açık uzak servis yolu var | Uzak erişim yoksa bu yol temel kurulumdan çıkar |
| V06 | V05 yolunda değiştirilmemiş varsayılan parola ve geniş yazma yetkisi var | L/E puanları yeniden verilir |
| V07 | Yerel servis hesabı paylaşılıyor; USB'den servis paketi yüklenebilir | USB yalnız veri aktarıyorsa R-03'ün yükleme zinciri düşer |
| V08 | Kapak/yeniden başlama denetimi bugün normal kontrol yazılımında | Bağımsız koruma varsa R-01/R-04 zinciri değişir |
| V09 | Yıkama tamamlanma bilgisi satış iznini etkileyen bir kontrol koşulu | Gerçek yöntem farklıysa SF-04 ve R-03 güncellenir |
| V10 | LAB5'in Component X v2.4 kaydı föyün temsili girdisidir | Gerçek kayıtlar ayrı raporda incelenir |

V05–V08 üreticide bulunmuş açıklar **değildir**. SMS bildirimi internetten programlama kanıtı, USB satış kaydı da program yükleme kanıtı sayılmaz. Kimyasal veya sıcak yıkama kabul edilmedi. Ayrı bir Safety PLC kurulu olduğu söylenmez; gereken koruma LAB4'te gereksinim olarak tanımlandı. Saha ve devre bilgisi olmadığından PLr/SIL atanmadı.

## Analizin değişeceği durumlar

- **Uzak erişim yoksa:** R-01'in uzak yolu çıkar; yerel ekran, USB ve bakım yolları kalır.
- **USB yalnız satış verisi aktarıyorsa:** R-03'ün program yükleme yolu geçersizleşir.
- **Karıştırıcıya erişim mümkün değilse:** mekanik senaryolar (R-01, R-04) yeniden puanlanır.
- **Gerçek temizlik ve ürün verisi farklıysa:** biyolojik senaryolar (R-02, R-03) gıda sorumlusuyla yeniden değerlendirilir.
- **Kontrolör ve yazılım sürümleri sahada okunursa:** LAB5 kararı gerçek kayıtlarla güncellenir.

## Yazılım araştırması (06.11.2026)

Üretici fotoğraflarında LS panel logosu görüldü; eXP20 ailesi yalnız **görsel aday**. Tam model ve kurulu işletim sistemi/runtime/PLC sürümü doğrulanmadı. XP-Builder ve XP-Remote 3.90.2221, XP-Manager 3.90.241211 üreticinin yayımladığı paket sürümleridir; otomatta **kurulu** sürümler değildir. Koşullu CVE adayları ve sürüm okuma adımları: [teknik rapor](../raporlar/Arminoks_Siber_Guvenlik_On_Degerlendirme_Raporu.pdf) · [yazılım/CVE envanteri](../raporlar/Arminoks_Yazilim_Surum_CVE_Envanteri.xlsx).

## Kaynaklar

| ID | Kaynak | Kullanım |
|---|---|---|
| T01 | Öğretmenin `2.1. lab_foyleri_genel.pdf` föyü | s.2–8: LAB1–7 görevleri |
| T02 | Öğretmenin `2.2 lab_foyleri_paketpro.pdf` föyü | Makineye uyarlama örneği |
| T03 | Öğretmenin `LAB3.pdf` ders notu | Slayt 23–33: ölçek; 43: görev; 46: tartışma |
| K01 | [Arminoks süt otomatı broşürü](https://www.arminoks.com/wp-content/uploads/2019/07/ARMINOKS-S%C3%9CT-OTOMATI-BRO%C5%9E%C3%9CR%C3%9C.pdf) | s.4–6: süt otomatı özellikleri |
| K02 | [NIST SP 800-82 Rev.3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) | OT güvenliği genel rehberi |
| K03 | [Regulation (EU) 2024/2847 — CRA](https://eur-lex.europa.eu/eli/reg/2024/2847/oj/eng) | LAB6 bildirim süreleri (Madde 14) |

> Bu föyün çıktısı **sistem sınırı ve varsayım listesi** → bütün Evidence Pack başlıklarının ortak dayanağıdır. Durum: **Taslak**.
