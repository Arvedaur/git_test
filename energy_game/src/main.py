from state import GameState
from npc import NPCTrader
from engine import play_day
from tutorial import show_tutorial

PORTFOLIOS = {
    "A": (80, 80, 40),
    "B": (100, 60, 40),
    "C": (60, 100, 40),
    "D": (80, 40, 60),
    "E": (40, 40, 100),
}

def main():
    show_tutorial()

    state = GameState()

    print("PORTFÖY SEÇ:")
    for k, v in PORTFOLIOS.items():
        print(f"{k}: Güneş {v[0]} | Rüzgar {v[1]} | Termik {v[2]}")

    choice = input("Seçim (A–E): ").upper()
    state.solar_mw, state.wind_mw, state.thermal_mw = PORTFOLIOS[choice]

    npc_count = int(input("NPC sayısı (1–4): "))
    npcs = [NPCTrader(f"NPC {i+1}", PORTFOLIOS[choice]) for i in range(npc_count)]

    DAYS = 3
    while state.day <= DAYS:
        print(f"\n=== GÜN {state.day} ===")
        print(f"Piyasa Talebi: {state.base_demand}")

        thermal = float(input("Termik kaç MW çalışsın?: "))
        prices = list(map(float, input("3 fiyat gir (örn 45 50 60): ").split()))

        result = play_day(state, npcs, prices, thermal)

        print("---- GÜN SONU ----")
        for k, v in result.items():
            print(f"{k}: {v}")

    print("\nOYUN BİTTİ")

if __name__ == "__main__":
    main()
