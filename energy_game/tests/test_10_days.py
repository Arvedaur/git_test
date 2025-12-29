import requests
from common import BASE_URL, assert_true

def test_10_days_simulation():
    requests.post(f"{BASE_URL}/start", params={"npc_count": 3})

    last_cash = None

    for day in range(10):
        r = requests.post(
            f"{BASE_URL}/step",
            json={"player_prices": [50], "player_thermal_dispatch": 100},
        )
        assert_true(r.status_code == 200, f"Day {day+1} failed")

        data = r.json()
        cash = data["player"]["cash"]

        assert_true(isinstance(cash, (int, float)), "Cash not numeric")

        last_cash = cash

    print("✔ 10-day simulation OK, final cash:", last_cash)
