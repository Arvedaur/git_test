BALANCING NOTES
Energy Market Simulator → Energy System Simulator

Version: 2.0
Scope: Generation / Transmission / Exchange (future-ready)

1. BU DOKÜMAN NE İŞE YARAR?

Bu doküman:

Oyundaki sayısal değerlerin neden o değerler olduğunu

Denge bozulduğunda hangi düğmeye basılacağını

Yeni feature eklendiğinde dengeyi nereden yeniden kuracağımızı

tanımlar.

Bu bir “ayar listesi” değil,
denge kararlarının anayasasıdır.

2. GENEL BALANCE FELSEFESİ
2.1 Ana İlke

Oyuncu her gün kazanmak zorunda değildir

Oyuncu kendi hatasıyla kaybettiğini anlayabilmelidir

RNG (rastgelelik) bahane değil, koşul olmalıdır

Eğer oyuncu şunu diyorsa:

“Ne yapsam fark etmiyor”

denge bozulmuştur.

2.2 “Tek Doğru Strateji” YASAĞI

Aşağıdakilerden biri oluşuyorsa alarm çalar:

Hep düşük fiyat kazanıyorsa

Hep termik açık oynamak kazandırıyorsa

Yenilenebilir fazlalığı hiç sorun yaratmıyorsa

Dominant strateji = zayıf oyun

3. GENERATION MODE – BALANCE ÇEKİRDEĞİ (ŞU AN)
3.1 Yenilenebilir Üretim Belirsizliği

Etkilediği şeyler:

Termik ihtiyacı

Curtailment

Fiyat stratejisi

Denge Kuralı

Yenilenebilir bazen fazla, bazen eksik gelmeli

Oyuncu her gün “termik açmalı mıyım?” diye düşünmeli

Alarm Durumları

Oyuncu termiği hiç açmıyorsa → belirsizlik düşük

Oyuncu termiği hep açıyorsa → belirsizlik aşırı

3.2 Termik Yakıt Maliyeti

Amaç:
Termiği “kontrollü ama pahalı” yapmak.

Durum	Sonuç
Yakıt ucuz	Termik OP
Yakıt pahalı	Termik ignore edilir
Doğru His

“Bugün açmasam mıydı?”
“Ama açmasaydım satış kaçacaktı.”

Bu ikilem yoksa balance yoktur.

3.3 Sabit Bakım (OPEX)

Amaç:
Oyuncuya şunu hissettirmek:

“Üretmesem de sistem çalışıyor.”

Alarm Durumları

Oyuncu uzun süre hiçbir şey yapmadan pozitifteyse → OPEX düşük

Oyuncu her gün zarar ediyorsa → OPEX yüksek

4. TALEP – FİYAT DENGESİ
4.1 Talep Elastikiyeti

Talep elastikiyeti:

Oyuncuya fiyatın önemli olduğunu öğretir

Ama fiyatı tek silah yapmaz

Denge Testi

Fiyatı %10 düşür → satış artıyor mu?

Fiyatı %10 artır → gelir bazen artıyor mu?

Eğer cevaplar hep aynıysa → katsayı yanlış.

4.2 Fiyat Dağılımı (Softmax)

SOFTMAX_K rekabetin sertliğini belirler.

Sertlik	Oyun Hissi
Çok yumuşak	Fiyat önemsiz
Çok sert	Tek oyuncu her şeyi alır

🎯 Hedef:
Ucuz olmak avantajlı, ama tek başına yeterli değil.

5. NPC DENGESİ
5.1 NPC Sayısı = Zorluk

NPC sayısı arttıkça:

Ortalama kâr düşmeli

Volatilite artmalı

Oyuncu “güvende” hissetmemeli

Eğer 4 NPC varken oyun hâlâ rahat oynanıyorsa → NPC pasif.

5.2 NPC Davranış Kalitesi

NPC’ler:

Optimal değildir

Ama aptal da değildir

Yanlış NPC Davranışları

Her gün aynı fiyat

Her gün aynı termik

Oyuncuya birebir tepki

NPC:

“Piyasa” gibi davranmalı,
“Rakip AI” gibi değil.

6. CURTAILMENT DENGESİ

Curtailment:

Ceza değildir

Uyarıdır

İdeal Dağılım

%0 → oyuncu düşünmüyor

%80 → oyuncu çaresiz

🎯 Hedef:
Curtailment grafiklerde can sıksın ama oyunu öldürmesin.

7. PORTFÖYLER ARASI DENGE
Portföy	Risk	Öğrenme
Yenilenebilir ağırlık	Yüksek	Orta
Dengeli	Orta	Yüksek
Termik ağırlık	Düşük	Düşük

Eğer:

Herkes termik ağırlığı seçiyorsa → yenilenebilir zayıf

Kimse termik istemiyorsa → termik aşırı pahalı

8. TRANSMISSION MODE – GELECEK BALANCE PRENSİPLERİ

(Şimdiden tanımlanır, sonra uygulanır)

8.1 Yeni Denge Hedefi

Transmission modunda:

Kâr ikincil

Sistem güvenliği birincil

Balance şu soruya göre yapılır:

“Bu karar sistem için mantıklı mı?”

8.2 Congestion Dengesi

Congestion:

Nadiren olursa anlamsız

Sürekli olursa sinir bozucu

🎯 Hedef:
Oyuncu congestion’ı öngörebilmeli,
ama her zaman engelleyememeli.

8.3 Redispatch Maliyeti

Redispatch:

Bedelsiz olmamalı

Ama oyunu kilitlememeli

Eğer oyuncu:

Redispatch’i umursamıyorsa → ucuz

Redispatch yüzünden oyun bitiyorsa → pahalı

9. EXCHANGE MODE – GELECEK BALANCE PRENSİPLERİ
9.1 Finansal Ürünler Asla Kopuk Olmamalı

Eğer:

Spot kötü ama futures kazanıyorsa
→ oyun “finans simi”ne döner

🎯 Kural:
Finansal başarı, fiziksel başarıdan tamamen kopuk olamaz.

9.2 Volatilite Dengesi

Volatilite yoksa → trading anlamsız

Aşırı volatilite → kumar hissi

Amaç:

Bilgi kazandıran volatilite

10. BALANCE DEĞİŞTİRME PROTOKOLÜ

Tek parametre değiştir

Monte Carlo çalıştır

Streamlit’te manuel oyna

Sonucu buraya not et

Eğer değişikliğin nedenini yazamıyorsan:

O değişiklik yapılmamalıdır.

11. BİLİNÇLİ DENGESİZLİKLER

Aşağıdakiler bilerek tam dengeli değildir:

Hava belirsizliği

NPC öngörülemezliği

Kısa vadeli zarar ihtimali

Çünkü:

Gerçek sistemler de dengeli değildir.