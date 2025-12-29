def show_tutorial():
    print("""
=====================================
ENERGY MARKET SIMULATOR – TUTORIAL
=====================================

BU OYUN NEYİ SİMÜLE EDER?
- Gün öncesi elektrik piyasasında üretim ve fiyatlama kararlarını
- Yenilenebilir belirsizliği (güneş / rüzgar)
- Termik santral dispatch riskini
- Rekabetçi fiyat savaşlarını

-------------------------------------
TEMEL KAVRAMLAR
-------------------------------------

TALEP (DEMAND)
- Gün başında açıklanan toplam piyasa ihtiyacıdır (MWh).
- Fiyat yükseldikçe gerçek talep düşebilir.

ÜRETİM
- Güneş & rüzgar: her gün otomatik ve rastgele üretilir.
- Termik: her gün SEN karar verirsin (0–maks MW).

TERMİK
- Avantaj: kontrol edilebilir
- Dezavantaj: yakıt maliyeti vardır (€/MWh)
- Yanlış zamanda açılırsa zarar yazdırır.

FİYAT TEKLİFİ
- Her gün 3 fiyat girersin.
- En rekabetçi (düşük) fiyatın piyasaya yansır.
- Daha düşük fiyat = daha çok satış, daha az marj.

SATIŞ PAYI
- Fiyata göre belirlenir.
- Ucuz olan daha çok satar (merit order mantığı).

STOK YOKTUR
- Satılamayan enerji KAYIPTIR.
- Elektrik depolanmaz (batarya yoksa).

MALİYET SKALASI
- Piyasa çok kalabalık ve küçükse sabit maliyetler bir miktar düşürülür.
- Bu, gerçek hayattaki kapasite mekanizmalarının soyutlamasıdır.

AMAÇ
- Her gün pozitif nakit yaratmak
- Yanlış dispatch ve fiyatlamadan kaçınmak

=====================================
""")
