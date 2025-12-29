def show_tutorial():
    print("""
========================================
ENERGY MARKET SIMULATOR – TUTORIAL
========================================

BU OYUN NEYİ SİMÜLE EDER?
- Elektrik gün-öncesi piyasasında
  üretim ve fiyatlama kararlarını.

TEMEL PRENSİPLER
----------------
• Talep her gün açıklanır (forecast).
• Güneş ve rüzgar otomatik üretir.
• Termik SANIN kontrolündedir.
• Elektrik stoklanamaz.
• Satılamayan üretim = KAYIP (curtailment).

TERMİK NEDEN RİSKLİ?
-------------------
• Yakıt maliyeti vardır.
• Yanlış zamanda açılırsa zarar yazar.
• Ama doğru günde hayat kurtarır.

FİYAT STRATEJİSİ
----------------
• Daha ucuz fiyat = daha fazla satış
• Ama daha düşük marj
• Piyasa tamamen rekabetçidir.

AMAÇ
-----
• Her gün pozitif nakit üretmek
• Talep – üretim – fiyat dengesini kurmak

========================================
""")
