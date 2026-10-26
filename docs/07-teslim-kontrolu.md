# Teslim kapsamı

Ana kaynak genel föy, uyarlama örneği PaketPro föyüdür. LAB3 ders notu ölçek ve tartışma soruları için kullanılmıştır. LAB6-7 dahil değildir. Orijinal föylerin boşluklarına yazılmamış; aynı görevleri karşılayan bölüm raporları hazırlanmıştır.

| Bölüm | Karşılanan görevler | Yanıt konumu |
|---|---|---|
| LAB1 | 8 ana soru, normal kontrol/koruma şeması | [LAB1](lab1-safety-architecture.md), L1-Q1-Q8 |
| LAB2 | 3 ana soru, 6 erişim kararı, 1 PaketPro uyarlaması; 5 senaryo yolu | [LAB2](lab2-zone-conduit.md), L2-A1-A3, B1-B6, P1 |
| LAB3 | 4 senaryo/4 profil, L/S/E gerekçeleri, puan, S3, önlem/sahip/tarih; 2 föy sorusu | [LAB3](lab3-risk-register.md), R-01-R-04, L3-Q1-Q2 |
| LAB3 tartışma | 5 ders sorusu; S1/27 hesabındaki tutarsızlığın açıklaması | [LAB3](lab3-risk-register.md), L3-T1-T5 |
| LAB4 | Başlangıç/hedef, 5 ilke, 2 bağımsızlık sorusu ve H01-H07 | [LAB4](lab4-secure-remote-access.md), L4-A, B1-B2 |
| LAB5 | 5 ana soru; bileşen/sürüm/erişim, yama ve telafi kararı | [LAB5](lab5-vulnerability-decision.md), L5-Q1-Q5 |
| Ek sorular | Her laboratuvarda 4; toplam 20 yanıt | L1-E1-E4 ile L5-E1-E4 arası |
| Destek | Makine profili, kaynak/varsayım listesi, SWOT, KT01-KT07 test planı | Profil ve SWOT belgeleri |

## Kayıtların durumu

| Kayıt | Durum |
|---|---|
| Makine özellikleri | Üretici broşürü ile sınırlı; model/seri no seçilmedi |
| Envanter ve riskler | Ürün bilgisi ve ders kabulleri ayrılmış eğitim analizi |
| SBOM / CVE / yama | Gerçek veri yok; föyün temsili kaydı üzerinden karar taslağı |
| Koruma doğrulaması | KT01-KT07 planı var; gerçek test yapılmadı |
| PDF / veri üretimi | Aynı Markdown kaynaklarından yeniden üretilebilir |
| Teknik kontrol | Güncel sonuç data/verification.json dosyasındadır; belge kontrolüdür |

Bütün soru kimlikleri data/question_manifest.json dosyasındadır. Kontrol aracı eksik soru, bozuk yerel bağlantı, yanlış risk çarpımı, kaynakla uyuşmayan veri ve PDF metin taşmalarını kontrol eder. Başarılı sonuç makinenin fiziksel emniyetinin doğrulandığı anlamına gelmez.
