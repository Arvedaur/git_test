ENERGY MARKET SIMULATOR
Game Design Document (GDD)

Version: 0.3
Status: Playable Prototype (Python / Streamlit)
Target Engine: Godot (v1.0)

1. GAME OVERVIEW
1.1 Oyun Türü

Energy Market Simulator;
strateji, ekonomi, simülasyon türlerini birleştiren, turn-based (günlük) bir karar oyunudur.

Oyuncu, bir elektrik üreticisi (asset owner / operator) rolünü üstlenir ve gün öncesi elektrik piyasasında rekabet eder.

Bu oyun:

Refleks değil karar oyunudur

Grafik aksiyondan ziyade ekonomik sonuçlara odaklanır

“Doğru his” değil doğru matematik öğretir

1.2 Hedef Kitle

Enerji sektörü profesyonelleri

Ekonomi / simülasyon oyunlarını seven oyuncular

“Frostpunk, Factorio, Cities Skylines” gibi sistem odaklı oyunlardan hoşlananlar

Eğitim amaçlı (üniversite, kurum içi eğitim) kullanıcılar

1.3 Oyunun Vaadi

“Elektrik piyasasında mesele sadece üretmek değil,
doğru zamanda, doğru fiyata, doğru miktarı üretmektir.”

Oyuncu:

Yenilenebilir belirsizliğiyle

Termik dispatch riskleriyle

Rekabetçi fiyat savaşlarıyla
karşı karşıya kalır.

Yanlış karar anında zarar yazar.
Doğru karar her zaman garanti değildir.

2. CORE GAMEPLAY LOOP

Oyun günlük döngüler halinde ilerler.

2.1 Günlük Oyun Akışı
1. Gün başı piyasa talebi açıklanır
2. Güneş ve rüzgar üretimi otomatik belirlenir
3. Oyuncu karar verir:
   - Termik kaç MW çalışacak?
   - 3 fiyat teklifi ne olacak?
4. NPC’ler kendi kararlarını verir
5. Piyasa clearing yapılır
6. Satış, gelir ve maliyet hesaplanır
7. Gün sonu raporu gösterilir


Bu döngü:

Öğretici

Tekrarlanabilir

Balanslanabilir
şekilde tasarlanmıştır.

3. PLAYER DECISIONS
3.1 Portföy Seçimi (Oyun Başında)

Oyuncu oyunun başında bir üretim portföyü seçer.
Bu seçim oyun boyunca değişmez.

Portföyler:

Güneş (MW)

Rüzgar (MW)

Termik (MW)

içerir.

Amaç:

Oyuncuya farklı risk profilleri sunmak

Tek bir “doğru” portföy yaratmamak

3.2 Termik Dispatch Kararı

Her gün oyuncu:

Termik santralini 0 – maksimum MW arasında çalıştırabilir.

Tasarım Mantığı

Termik kontrol edilebilir

Ama yakıt maliyeti vardır

Yanlış zamanda açılırsa direkt zarar

Termik:

Sigorta gibidir

Ama pahalı bir sigorta

3.3 Fiyat Teklifleri

Oyuncu her gün 3 fiyat girer.

Örnek:

45 / 50 / 60

Aktif Fiyat

Piyasa, oyuncunun en rekabetçi (en düşük) fiyatını dikkate alır.

Bu tasarım:

Gerçek piyasa teklif mantığının basitleştirilmiş hâlidir

Oyuncuyu fiyat bandı düşünmeye zorlar

4. MARKET & COMPETITION
4.1 NPC’ler

Oyunda oyuncuya karşı NPC üreticiler vardır.

NPC’ler:

Oyuncu ile aynı portföy yapısını kullanır

Fiyatlarını oyuncuya göre konumlandırır

Termiklerini genellikle kısmi çalıştırır

NPC’ler:

Çok akıllı değildir

Ama öngörülemezdir

Bu bilinçli bir tercihtir:

Amaç oyuncuyu yenmek değil,
piyasayı temsil etmek.

4.2 Rekabet Seviyesi

Rekabet:

NPC sayısına bağlıdır

NPC sayısı arttıkça:

Satış payı düşer

Fiyat kırma artar

Kâr marjı daralır

Bu, gerçek hayattaki:

Yoğun rekabetli yenilenebilir piyasaların
soyutlamasıdır.

5. DEMAND SYSTEM
5.1 Açıklanan Talep (Forecast)

Her gün başında piyasa talebi açıklanır.

Bu:

Gün öncesi sistem yükü tahminini temsil eder

Rastgele ama yumuşak dalgalıdır

Talep:

Bir önceki güne bağlı olarak değişir

Aşırı zıplamaz

5.2 Gerçek Talep (Price Elasticity)

Talep, fiyatlara bağlı olarak gerçekleşir.

Basit formül:

Gerçek Talep = Açıklanan Talep × (1.25 − En Düşük Fiyat / 100)


Sonuç:

Fiyat yükseldikçe talep düşer

Fiyat çok düşerse talep artar

Bu:

Tüketici davranışının

Talep elastikiyetinin
basitleştirilmiş hâlidir.

6. PRODUCTION SYSTEM
6.1 Güneş & Rüzgar

Güneş ve rüzgar üretimi her gün rastgele belirlenir

Kapasitenin belirli bir yüzdesi üretilir

Amaç:

Hava belirsizliğini yansıtmak

Oyuncuya “kontrolsüz risk” vermek

6.2 Termik

Oyuncu tarafından kontrol edilir

Yakıt maliyeti vardır

Fazla açılırsa zarar

Az açılırsa satış kaçırma riski

Bu, oyunun en kritik kararıdır.

7. MARKET CLEARING & SALES
7.1 Fiyat Bazlı Satış Payı

Satış payı:

Fiyata göre belirlenir

Daha ucuz üretici daha çok satar

Teknik olarak:

Softmax benzeri bir dağılım kullanılır

Bu:

Merit order mantığını

Aşırı sert olmayan bir şekilde simüle eder

7.2 Satış ve Curtailment

Stok YOKTUR.

Satış:

Satılan = min(Hedef Talep Payı, Toplam Üretim)


Satılamayan üretim:

Curtailment

Parasal karşılığı yok

Bir sonraki güne taşınmaz

Bu karar:

Fiziksel gerçeklikle uyumlu

Oyunu daha sert ama doğru yapar

8. COST & ECONOMY
8.1 Gelir
Gelir = Satılan MWh × Aktif Fiyat


Basit, net ve anlaşılır.

8.2 Maliyetler
Sabit Bakım

Güneş

Rüzgar

Termik

Her gün ödenir.

Termik Yakıt
Yakıt Maliyeti = Termik Üretim × €/MWh


Termik üretimin anında bedeli vardır.

8.3 Talep / Aktör Maliyet Skalası

Sabit maliyetler:

Piyasa çok küçük ve kalabalıksa düşürülür

Piyasa genişse normale yaklaşır

Bu:

Kapasite mekanizmaları

Destekler

Ölçek avantajlarının
soyutlamasıdır.

9. PROFIT & LOSS
Kâr = Gelir − (Sabit Bakım + Yakıt)


Bu:

EBITDA benzeri bir bakış açısıdır

Finansal okuryazarlık kazandırır

10. TUTORIAL & ONBOARDING

Oyunda tutorial:

Oyunun başında gösterilir

Ayrı bir metin havuzundan beslenir

Tutorial:

Oyunu öğretir

Ama strateji vermez

Amaç:

Oyuncuya cevap değil,
doğru soruları vermek.

11. DIFFICULTY & PROGRESSION

Zorluk NPC sayısıyla artar

Talep dalgalanması oyunu doğal olarak zorlaştırır

Oyuncu:

Deneyimle

Hata yaparak
öğrenir

Bu bilinçli bir tasarımdır.

12. TECHNICAL ARCHITECTURE
12.1 Katmanlar

core/ → oyun motoru

ui/ → Streamlit / Terminal

config/ → balancing

simulations/ → analiz

tools/ → export & replay

UI ve motor tamamen ayrıdır.

12.2 Godot Geçiş Planı

Python core → Godot scripts

UI tamamen yeniden yazılır

Matematik ve balans aynen korunur

13. ROADMAP (ÖZET)
v0.3 (Şu an)

Python

Streamlit

Playable prototype

v0.4

Grafikler

Replay izleme

Akıllı NPC

v1.0

Godot

Görsel UI

Save / Load

14. TASARIM FELSEFESİ (ÖNEMLİ)

Bu oyun:

Oyuncuyu kandırmaz

“Eğlenceli olsun diye” yalan söylemez

Gerçek hayattaki acıyı öğretir

Ama aynı zamanda:

Öğreticidir

Adildir

Sistematik düşünmeyi teşvik eder

15. SON SÖZ

Energy Market Simulator:

Bir “oyun”dan çok,
oynanabilir bir ekonomik modeldir.

Başarı:

Şansa değil

Deneyime ve muhakemeye bağlıdır.