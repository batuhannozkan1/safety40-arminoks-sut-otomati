# Teslim kontrolü | Föy ve yanıt eşleştirmesi

Kapsam: LAB 1–5. Genel föy ana görev kaynağı, PaketPro uyarlama örneği, LAB3 ders notu ölçek ve tartışma kaynağıdır. LAB6–7 dahil değildir.

## Ana görevler, kararlar ve ders tartışmaları

| Kimlik | Karşılanan görev | Yanıt |
|---|---|---|
| L1-Q1 | Bu makinede tehlike nedir? İnsan neyden zarar görür? | [LAB 1](lab1-safety-architecture.md) |
| L1-Q2 | Safety function (emniyet fonksiyonu) hangisidir? | [LAB 1](lab1-safety-architecture.md) |
| L1-Q3 | Safety-related control system nerede? Şemada işaretleyin. | [LAB 1](lab1-safety-architecture.md) |
| L1-Q4 | Normal PLC ile Safety PLC farkı nedir? | [LAB 1](lab1-safety-architecture.md) |
| L1-Q5 | PLr / SIL neden var? Bu fonksiyon için neden önemli? | [LAB 1](lab1-safety-architecture.md) |
| L1-Q6 | Safe state (güvenli durum) nedir? | [LAB 1](lab1-safety-architecture.md) |
| L1-Q7 | Safety function hangi dijital bağımlılıklara sahip? | [LAB 1](lab1-safety-architecture.md) |
| L1-Q8 | Siber müdahale hangi noktadan bu fonksiyonu bozar? | [LAB 1](lab1-safety-architecture.md) |
| L2-A1 | Hangi varlıklar aynı bölgede? Bölgeleri adlandırıp gruplandırın. | [LAB 2](lab2-zone-conduit.md) |
| L2-A2 | Safety PLC'yi hangi bölgeye koydunuz, neden? | [LAB 2](lab2-zone-conduit.md) |
| L2-A3 | Conduit'ler nerede? Her geçişte ne kontrol edilecek? | [LAB 2](lab2-zone-conduit.md) |
| L2-B1 | Aracı: seçim ve gerekçe | [LAB 2](lab2-zone-conduit.md) |
| L2-B2 | Tünel: seçim ve gerekçe | [LAB 2](lab2-zone-conduit.md) |
| L2-B3 | Kimlik: seçim ve gerekçe | [LAB 2](lab2-zone-conduit.md) |
| L2-B4 | Hesap: seçim ve gerekçe | [LAB 2](lab2-zone-conduit.md) |
| L2-B5 | Kayıt: seçim ve gerekçe | [LAB 2](lab2-zone-conduit.md) |
| L2-B6 | Zamanlama: seçim ve gerekçe | [LAB 2](lab2-zone-conduit.md) |
| L2-P1 | PaketPro varyantı: Açık uzak bakım modülü hangi bölgeye düşüyor; orada kalabilir mi? | [LAB 2](lab2-zone-conduit.md) |
| L3-Q1 | En yüksek öncelikli senaryonuz hangisi? Neden? | [LAB 3](lab3-risk-register.md) |
| L3-Q2 | S=3 olup skoru düşük kalan senaryo var mı? Nasıl görünür kılacaksınız? | [LAB 3](lab3-risk-register.md) |
| L3-T1 | Aynı kapıyı iki farklı profil kullanırsa skor değişir mi? | [LAB 3](lab3-risk-register.md) |
| L3-T2 | Skoru 27 ama S1 olan senaryo mu, skoru 3 olan S3 mü önce? | [LAB 3](lab3-risk-register.md) |
| L3-T3 | Emniyete dokunmayan siber senaryo Register'a girmeli mi? | [LAB 3](lab3-risk-register.md) |
| L3-T4 | Tedarikçinin güvenli beyanına ne kadar güvenirsiniz; hangi kanıt gerekir? | [LAB 3](lab3-risk-register.md) |
| L3-T5 | Register ne zaman tekrar puanlanmalı? | [LAB 3](lab3-risk-register.md) |
| L4-A | Görev A: Başlangıç ve hedef mimari; beş ilke | [LAB 4](lab4-secure-remote-access.md) |
| L4-B1 | Saldırgan bütün önlemlere rağmen içeri girerse emniyet fonksiyonu etkilenir mi? Neden? | [LAB 4](lab4-secure-remote-access.md) |
| L4-B2 | Emniyetin kontrol sisteminden ve uzak bakım yolundan bağımsızlığı için gereksinimi yazın. | [LAB 4](lab4-secure-remote-access.md) |
| L5-Q1 | Bu CVE sizi gerçekten etkiliyor mu? Üç şartı kontrol edin. | [LAB 5](lab5-vulnerability-decision.md) |
| L5-Q2 | Üretimi hemen durdurur musunuz? Neden / neden değil? | [LAB 5](lab5-vulnerability-decision.md) |
| L5-Q3 | Yamayı doğrudan mı uygularsınız, önce test mi? Nerede test? | [LAB 5](lab5-vulnerability-decision.md) |
| L5-Q4 | Yama safety validation'ı etkiliyor mu? Nasıl anlarsınız? | [LAB 5](lab5-vulnerability-decision.md) |
| L5-Q5 | Yama mümkün değilse telafi edici önlem ne olur? | [LAB 5](lab5-vulnerability-decision.md) |

## Makineye özgü ek sorular

Beş laboratuvarda dörder, toplam **20 ek soru** yanıtlandı. Eksik saha verileri gerçekmiş gibi tamamlanmadı.

| Kimlik | Ek soru | Yanıt |
|---|---|---|
| L1-E1 | Her şeyi kapatmak neden her zaman güvenli değildir? | [LAB 1](lab1-safety-architecture.md) |
| L1-E2 | Panel normal sıcaklık gösteriyorsa satış yapılabilir mi? | [LAB 1](lab1-safety-architecture.md) |
| L1-E3 | Reset neden başlatma olmamalı? | [LAB 1](lab1-safety-architecture.md) |
| L1-E4 | Emniyet bağımsızlığını nasıl sınarız? | [LAB 1](lab1-safety-architecture.md) |
| L2-E1 | SMS modülü internet saldırı yolu mudur? | [LAB 2](lab2-zone-conduit.md) |
| L2-E2 | Satış verisi alan USB neden önemlidir? | [LAB 2](lab2-zone-conduit.md) |
| L2-E3 | Aynı VLAN yerine farklı VLAN yeterli koruma mıdır? | [LAB 2](lab2-zone-conduit.md) |
| L2-E4 | Ödeme başarısı koruma koşullarını aşabilir mi? | [LAB 2](lab2-zone-conduit.md) |
| L3-E1 | İnternet bağlantısı hiç yoksa sonuç ne olur? | [LAB 3](lab3-risk-register.md) |
| L3-E2 | Temizlik yalnız soğuk suyla yapılıyorsa? | [LAB 3](lab3-risk-register.md) |
| L3-E3 | Önlem sonrası skor düşmüyorsa önlem işe yaramaz mı? | [LAB 3](lab3-risk-register.md) |
| L3-E4 | En çok tartışılabilecek puan hangisi? | [LAB 3](lab3-risk-register.md) |
| L4-E1 | Bakımcı ekranı görebiliyorsa program da yükleyebilir mi? | [LAB 4](lab4-secure-remote-access.md) |
| L4-E2 | Bağlantı kesilince ne olur? | [LAB 4](lab4-secure-remote-access.md) |
| L4-E3 | Ayrı Safety PLC varsa tamamen güvende miyiz? | [LAB 4](lab4-secure-remote-access.md) |
| L4-E4 | Öncelikli risk zinciri nerede kırılır? | [LAB 4](lab4-secure-remote-access.md) |
| L5-E1 | Gerçek CVE bulmadan LAB5 tamamlanabilir mi? | [LAB 5](lab5-vulnerability-decision.md) |
| L5-E2 | Hash doğruysa paket güvenilir midir? | [LAB 5](lab5-vulnerability-decision.md) |
| L5-E3 | Geri dönüş desteklenmiyorsa ne yaparız? | [LAB 5](lab5-vulnerability-decision.md) |
| L5-E4 | Kapanış için hangi somut sonuç gerekir? | [LAB 5](lab5-vulnerability-decision.md) |

## Teslim kalitesi ve kapsam sınırı

| Kontrol | Tamamlanma ölçütü |
|---|---|
| Kimlik ve kapsam | Ad, öğrenci numarası, atanan makine; LAB1–5 |
| Bilgi ayrımı | D/V/H tanımları; gerçek ve eğitim modeli ayrımı |
| LAB1 | 8 ana soru, SF tablosu, normal/koruma diyagramı |
| LAB2 | Altı kategori, 6 kapı, zone/conduit, 6 erişim kararı |
| LAB3 | 4 senaryo/4 profil; L/S/E gerekçeleri; S3, sahip, tarih, hedef risk |
| LAB4 | Başlangıç/hedef ve 7 test edilebilir gereksinim |
| LAB5 | Üç koşullu etkilenme; temsili CVE; belirsiz karar; SBOM/yama kayıt taslakları |
| İlave kapsam | 20 ek soru; 5 ders tartışması; SWOT ve doğrulama planı |
| Çıktı | 8 bölüm PDF + 1 birleşik PDF; Markdown; risk JSON/CSV; üretim/kontrol araçları |
| Sınır | Gerçek cihaz testi, yama kurulumu, gerçek SBOM ve sertifikasyon yok |
