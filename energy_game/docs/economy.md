ECONOMY SYSTEM
Energy Market Simulator
1. EKONOMİK TASARIMIN AMACI

Energy Market Simulator’ın ekonomi sistemi şu hedeflerle tasarlanmıştır:

Oyuncuya kâr = karar ilişkisini net göstermek

Enerji piyasalarında:

belirsizlik,

rekabet,

maliyet baskısı
üçgenini öğretmek

Gerçek dünyadaki piyasa dinamiklerini oynanabilir ama dürüst şekilde soyutlamak

Bu oyun:

“Para kazanma oyunu” değildir

“Ekonomik karar simülatörü”dür

2. EKONOMİNİN TEMEL PRENSİPLERİ

Ekonomi sistemi şu prensiplere dayanır:

Anlık üretim, anlık satış

Stok yok

Nakit tek kümülatif kaynaktır

Her maliyet gerçek hayattaki bir karşılığı temsil eder

Zarar etmek mümkündür ve normaldir

3. PARA BİRİMİ VE ÖLÇEK
3.1 Para Birimi

Oyunda kullanılan para birimi:

Euro (€)

Bu:

Avrupa enerji piyasalarına referans verir

Oyuncuya tanıdık bir ekonomik ölçek sunar

3.2 Enerji Birimi

Tüm üretim ve talep:

MWh (Megawatt-saat) cinsindendir

Bu:

Saatlik detay olmadan

Günlük toplam enerji mantığını temsil eder

4. GELİR MEKANİĞİ
4.1 Gelirin Tanımı

Oyuncunun geliri yalnızca satılan enerji üzerinden oluşur.

Formül:

Gelir = Satılan Enerji (MWh) × Aktif Piyasa Fiyatı (€/MWh)

4.2 Aktif Piyasa Fiyatı

Aktif fiyat:

Oyuncunun verdiği 3 teklif arasından

en düşük (en rekabetçi) olanıdır

Bu mekanik:

“Fiyat bandı” düşünmeyi öğretir

Gerçek hayattaki teklif stratejilerinin sadeleştirilmiş hâlidir

4.3 Satılamayan Enerji

Satılamayan enerji:

Gelir yaratmaz

Curtailment olarak kabul edilir

Ekonomik karşılığı sıfırdır

Oyunda “belki yarın satarım” yoktur.

5. MALİYET MEKANİKLERİ

Ekonomi sistemi iki ana maliyet türü içerir:

Sabit maliyetler (OPEX)

Değişken maliyetler (yakıt)

5.1 Sabit Bakım Maliyetleri (OPEX)

Her üretim türü için günlük sabit bakım maliyeti vardır:

Güneş

Rüzgar

Termik

Bu maliyetler:

Üretim yapılsa da yapılmasa da oluşur

Günlük bazda düşülür

Amaç:

Santral işletme gerçekliğini yansıtmak

“Üretmesem de bedeli var” hissini vermek

5.2 Termik Yakıt Maliyeti

Termik santral için:

Üretilen her MWh başına yakıt maliyeti vardır

Formül:

Yakıt Maliyeti = Termik Üretim (MWh) × Yakıt Birim Maliyeti (€/MWh)


Özellikler:

Değişkendir

Üretim arttıkça artar

Doğrudan kârı etkiler

Bu mekanik:

Termiği “kontrollü ama pahalı” yapar

6. KÂR (PROFIT) HESAPLAMASI
6.1 Günlük Kâr

Oyunda “kâr” şu şekilde hesaplanır:

Kâr = Gelir − (Sabit Bakım + Yakıt Maliyeti)


Bu yaklaşım:

EBITDA benzeri bir bakış sunar

Finansal karmaşıklığı sınırlı tutar

6.2 Kümülatif Nakit

Oyuncunun asıl performans metriği:

Toplam Nakit (Cash)

Her gün sonunda:

Toplam Nakit = Önceki Nakit + Günlük Kâr


Oyun:

Bilanço

Borç

Finansman
içermez

Ama:

Nakit akışı hissini güçlü verir

7. TALEP VE FİYATIN EKONOMİYE ETKİSİ
7.1 Talep Elastikiyeti

Gerçekleşen talep:

Ortalama piyasa fiyatına bağlıdır

Sonuç:

Düşük fiyat → daha yüksek talep

Yüksek fiyat → talep daralması

Bu:

Tüketici davranışının

Basitleştirilmiş bir modelidir

7.2 Fiyat Kırma Riski

Düşük fiyat:

Daha fazla satış payı sağlar

Ama birim geliri düşürür

Yüksek fiyat:

Birim geliri artırır

Ama talep ve satış payını düşürür

Oyuncu:

“Ne kadar satarım?” ile
“Kaça satarım?” arasında kalır.

Bu oyunun ekonomik kalbidir.

8. REKABET VE EKONOMİ
8.1 NPC Sayısının Etkisi

NPC sayısı arttıkça:

Toplam talep paylaşılır

Satış payı düşer

Fiyat baskısı artar

Kâr marjları daralır

Bu:

Rekabetçi piyasa hissini güçlendirir

Oyuncunun tek başına “piyasa yapıcı” olmasını engeller

8.2 NPC Davranışlarının Ekonomik Etkisi

NPC’ler:

Aşırı agresif değildir

Genellikle orta fiyat verir

Termiği sınırlı kullanır

Sonuç:

Oyuncu kötü oynarsa zarar eder

Ama her zaman “NPC yüzünden kaybettim” hissi oluşmaz

9. CURTAILMENT’IN EKONOMİK ANLAMI

Curtailment:

Satılamayan üretimi temsil eder

Gelir getirmez

Ama maliyet yaratmış olabilir

Bu:

Yenilenebilir fazlalığı

Yanlış dispatch

Yanlış fiyatlama
sonucunda oluşur

Curtailment:

Oyunun “sessiz cezasıdır”.

10. EKONOMİDE BİLİNÇLİ OLARAK OLMAYAN ŞEYLER

Bu versiyonda bilerek yer almayan ekonomik unsurlar:

Depolama gelirleri

Kapasite ödemeleri

Yan hizmetler

Emisyon / karbon maliyetleri

Forward / futures kontratlar

Saatlik fiyat volatilitesi

Sebep:

Öğrenme eğrisini sade tutmak

Çekirdeği sağlam kurmak

11. EKONOMİK GENİŞLEME POTANSİYELİ

Bu ekonomi sistemi ileride şu modüllerle genişletilebilir:

Batarya ve depolama

Karbon fiyatlaması

Negatif fiyatlar

PPA’lar

Uzun vadeli kontratlar

Farklı piyasa bölgeleri

Mevcut çekirdek:

Bu genişlemeleri kırılmadan taşıyabilecek şekilde tasarlanmıştır.

12. EKONOMİK TASARIMIN EĞİTİCİ HEDEFİ

Bu oyunun ekonomisi şunu öğretir:

Çok üretmek ≠ çok kazanmak

Yüksek fiyat ≠ yüksek kâr

Kontrol edilebilirlik ≠ düşük risk

Oyuncu zamanla şunu fark eder:

Kâr, matematik kadar muhakemedir.

13. SON NOT

Bu ekonomi sistemi:

Testlerle doğrulanmıştır

UI’den bağımsızdır

Godot portunda aynen korunacaktır

Dolayısıyla:

Ekonomi değişirse → oyunun ruhu değişir
UI değişirse → ekonomi değişmez