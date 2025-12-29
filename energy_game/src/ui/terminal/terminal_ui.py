from core.engine import play_day

def run_terminal_game(state, npcs, days=3):
    print("=== TERMINAL DEBUG MODE ===")

    while state.day <= days:
        print(f"\n--- DAY {state.day} ---")

        thermal = float(input("Thermal dispatch (MW): "))
        prices = list(map(float, input("3 prices (e.g. 45 50 60): ").split()))

        result = play_day(state, npcs, prices, thermal)

        print("\nRESULT:")
        for k, v in result.items():
            print(f"{k}: {v}")
