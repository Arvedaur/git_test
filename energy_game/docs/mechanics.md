Energy Market Simulator
1. GENEL MEKANİK FELSEFESİ

Energy Market Simulator’ın mekanikleri şu prensiplere dayanır:

Basit ama gerçekçi

Deterministik çekirdek + rastlantısal çevre

Oyuncuya “kontrol hissi” verirken, tam kontrol yanılsaması yaratmaz

Fiziksel ve ekonomik gerçeklere aykırı mekanik içermez

Bu oyunda:

Stok yoktur

Üretim anlıktır

Satılamayan enerji kaybolur

Yanlış karar anında bedel ödetir

2. ZAMAN VE TUR YAPISI
2.1 Gün Kavramı

Oyun günlük turlar halinde ilerler.

Her gün:

Bağımsız bir piyasa clearing sürecidir

Bir önceki günün kararları doğrudan taşınmaz

Sadece finansal sonuçlar (nakit) kümülatiftir

Gerçek hayattaki “gün öncesi piyasası” soyutlanmıştır.

2.2 Günlük Akış

Bir gün şu adımlardan oluşur:

Piyasa talebi belirlenir

Yenilenebilir üretim (güneş + rüzgar) oluşur

Oyuncu karar verir:

Termik dispatch

3 fiyat teklifi

NPC’ler kendi kararlarını verir

Piyasa clearing yapılır

Gelir, maliyet ve kâr hesaplanır

Gün sonu raporu ve grafikler güncellenir

3. ÜRETİM MEKANİKLERİ
3.1 Üretim Türleri

Oyunda üç üretim türü vardır:

Tür	Kontrol	Maliyet	Belirsizlik
Güneş	❌	Sabit	Yüksek
Rüzgar	❌	Sabit	Yüksek
Termik	✅	Yakıt	Düşük
3.2 Güneş ve Rüzgar Üretimi

Güneş ve rüzgar oyuncu tarafından kontrol edilemez

Her gün kapasitenin belirli bir yüzdesi üretilir

Bu oran rastgeledir

Amaç:

Hava koşullarını

Yenilenebilir belirsizliğini
soyutlamak

Oyuncu yenilenebilir üretimi “tahmin eder”, yönetmez.

3.3 Termik Üretim (Dispatch)

Termik santral:

Oyuncunun tek doğrudan kontrol ettiği üretimdir

Günlük olarak 0 – maksimum MW aralığında seçilir

Özellikleri:

Anında devreye girer

Yakıt maliyeti vardır

Gereksiz çalıştırılırsa zarar yazar

Termik:

“Sigorta”dır ama pahalıdır.

4. PORTFÖY MEKANİĞİ
4.1 Portföy Seçimi

Oyuncu oyun başında bir portföy seçer.

Portföy:

Güneş MW

Rüzgar MW

Termik MW

değerlerinden oluşur.

Bu seçim:

Oyun boyunca değişmez

Oyuncunun risk profilini belirler

4.2 NPC Portföyleri

NPC’ler:

Oyuncu ile aynı portföy büyüklüğünü kullanır

Ama kararlarını farklı verir

Bu:

Rekabeti “adil ama zor” yapar

Oyuncunun başarısını gerçekten ölçer

5. TALEP MEKANİĞİ
5.1 Açıklanan Talep (Base Demand)

Her gün başında:

Bir piyasa talebi açıklanır

Bu değer rastgele ama yumuşak değişir

Bu:

Gün öncesi sistem yükü tahminini temsil eder

5.2 Gerçek Talep (Price Elasticity)

Gerçekleşen talep:

Fiyatlara bağlıdır

Düşük fiyat → daha yüksek talep

Yüksek fiyat → talep düşüşü

Basitleştirilmiş formül:

Gerçek Talep = Base Demand × Talep Katsayısı


Talep katsayısı:

Ortalama piyasa fiyatına göre belirlenir

Bu:

Talep elastikiyetinin

Oyuna uygun bir soyutlamasıdır

6. FİYAT MEKANİĞİ
6.1 Oyuncu Fiyat Teklifleri

Oyuncu her gün 3 fiyat girer.

Örnek:

45 50 60


Bu:

Farklı piyasa senaryolarına hazırlık anlamına gelir

Oyuncuyu “tek fiyat” düşüncesinden çıkarır

6.2 Aktif Fiyat Seçimi

Piyasa:

Oyuncunun verdiği fiyatlar arasından

en rekabetçi (en düşük) olanı kullanır

Bu:

Merit order mantığının

sadeleştirilmiş bir versiyonudur

7. PİYASA CLEARING MEKANİĞİ
7.1 Satış Payı

Toplam talep:

Oyuncu ve NPC’ler arasında paylaşılır

Paylaşım:

Fiyatlara göre yapılır

Daha ucuz üretici daha fazla satar

Bu dağılım:

Sert değildir

Softmax benzeri bir fonksiyon kullanır

Amaç:

Gerçekçi ama oynanabilir bir rekabet yaratmak

7.2 Satılan Enerji

Satılan enerji şu şekilde hesaplanır:

Satılan = min(Üretim, Talep Payı)

7.3 Curtailment

Satılamayan enerji:

Curtailment olarak kabul edilir

Gelir getirmez

Bir sonraki güne taşınmaz

Oyunda stok mekanizması YOKTUR.

Bu karar:

Fiziksel gerçeklikle uyumludur

Oyunu daha sert ama doğru yapar

8. MALİYET MEKANİĞİ
8.1 Sabit Bakım Maliyetleri

Her üretim türü için:

Günlük sabit bakım maliyeti vardır

Üretim yapılıp yapılmamasına bakılmaz

Bu:

OPEX’in soyutlamasıdır

8.2 Termik Yakıt Maliyeti

Termik üretim:

Üretilen MWh başına yakıt maliyeti doğurur

Formül:

Yakıt Maliyeti = Termik Üretim × €/MWh


Bu maliyet:

Anında düşülür

Gecikmeli değildir

9. GELİR VE KÂR
9.1 Gelir
Gelir = Satılan MWh × Aktif Fiyat

9.2 Kâr
Kâr = Gelir − (Sabit Bakım + Yakıt)


Bu:

EBITDA benzeri bir bakış açısıdır

Finansal okuryazarlığı teşvik eder

10. NPC DAVRANIŞ MEKANİKLERİ

NPC’ler:

Basit heuristikler kullanır

Genellikle:

Orta fiyat

Kısmi termik dispatch
tercih eder

Ama:

Her gün birebir aynı davranmazlar

Amaç:

Piyasayı temsil etmek

Oyuncuyu ezmek değil

11. GERİ BİLDİRİM MEKANİKLERİ

Oyuncu şu geri bildirimleri alır:

Gün sonu metrikleri

Canlı grafikler:

Nakit

Curtailment

Üretim dağılımı

Fiyat vs talep

Bu grafikler:

“Ne oldu?” sorusunu

“Neden oldu?”ya dönüştürür

12. MEKANİK SINIRLARI (BİLİNÇLİ)

Bu versiyonda bilinçli olarak yoktur:

Depolama

Stok

Forward kontratlar

Saatlik fiyatlar

Şebeke kısıtları

Emisyon maliyetleri

Ama:

Mekanikler bu genişlemelere açıktır

13. MEKANİKLERİN EĞİTİCİ AMACI

Bu oyunun mekanikleri:

“En çok üret” demez

“En pahalıya sat” da demez

Şunu öğretir:

Doğru miktarı, doğru zamanda, doğru fiyata üret.

14. SON NOT

Bu mekanik seti:

Testlerle korunmaktadır

UI’den bağımsızdır

Godot portunda birebir korunacaktır

Bu nedenle:

Mechanics değişirse → oyun değişir
UI değişirse → oyun değişmez