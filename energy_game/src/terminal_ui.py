def show_intro():
    print("""
ENERGY TRADER – HOŞ GELDİN

Akış:
1) Oyun ayarları: kaç NPC olacak seçersin
2) Her gün başında piyasa talebi açıklanır (forecast)
3) Sen 3 fiyat teklifi verirsin
4) NPC'ler teklif verir
5) Piyasa clearing olur: fiyat sıralamasına göre satış payları dağıtılır
6) Gün sonu raporu çıkar

Hedef:
30 gün sonunda nakit ve riskini yöneterek ayakta kalmak.
""")


def choose_npc_count():
    print("""
KAÇ RAKİP ŞİRKET (NPC)?

1 - Az rekabet
2 - Orta rekabet
3 - Yoğun rekabet
""")
    while True:
        c = input("Seçim (1/2/3): ").strip()
        if c in ("1", "2", "3"):
            return int(c)
        print("Geçersiz seçim.")


def show_demand_announcement(day, base_demand):
    print(f"\n=== GÜN {day} – PİYASA AÇILIŞI ===")
    print(f"Piyasa Talebi (Forecast): {base_demand} MWh")
    print("Not: Gerçek talep, en ucuz fiyatın etkisiyle biraz değişebilir.")


def get_player_inputs():
    """
    İstediğin akışa göre:
      - Talep oyuncudan alınmıyor (gün başı açıklanıyor)
      - Oyuncu üretim + 3 fiyat veriyor
    """
    prod = float(input("Bugün üretimin (MWh): ").strip())
    parts = input("3 fiyat teklifi (örn: 45 55 70): ").split()
    prices = [float(x) for x in parts]
    if len(prices) != 3:
        raise ValueError("Tam olarak 3 fiyat girmelisin (örn: 45 55 70).")
    return prod, prices


def render_day_report(report):
    print("\n--- PİYASA SONUCU / RAPOR ---")
    print(f"Base Demand: {report['base_demand']} MWh")
    print(f"Ref Price (en ucuz): {report['ref_price']} €/MWh")
    print(f"Real Demand: {report['real_demand']} MWh")
    print()

    print("Teklif Sıralaması (ucuzdan pahalıya):")
    for actor, price in report["offers_sorted"]:
        print(f"  - {actor}: {price} €/MWh")

    print("\nPaylar:")
    for actor, share in report["shares"].items():
        print(f"  - {actor}: {share*100:.1f}%")

    print("\nSENİN SONUCUN:")
    print(f"  En iyi fiyatın: {report['player_best_price']} €/MWh")
    print(f"  Üretim: {report['player_production']} MWh")
    print(f"  Hedef satış (payına düşen): {report['player_target_sales']} MWh")
    print(f"  Satış: {report['player_sold']} MWh")
    print(f"  Shortfall: {report['player_shortfall']} MWh")
    print(f"  Gelir: {report['player_revenue']} €")
    print(f"  Ceza: -{report['player_penalty']} €")
    print(f"  Risk kaybı: -{report['risk_loss']} €")
    print(f"  Nakit: {report['cash']} €")
    print(f"  Stok: {report['inventory']} MWh")
    print(f"  Risk: {report['risk']}")

    if report["npcs"]:
        print("\nNPC ÖZETİ:")
        for npc in report["npcs"]:
            print(
                f"  - {npc['name']} ({npc['strategy']}): "
                f"fiyat={npc['offer_price']} share={npc['share']*100:.1f}% "
                f"satış={npc['sold']} hedef={npc['target_sales']} stok={npc['inventory']}"
            )
