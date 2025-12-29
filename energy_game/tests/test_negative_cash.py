import requests
from common import BASE_URL, assert_true

def test_negative_cash_guard():
    requests.post(f"{BASE_URL}/start", params={"npc_count": 2})

    for _ in range(10):
        r = requests.post(
            f"{BASE_URL}/step",
            json={"player_prices": [80], "player_thermal_dispatch": 200},
        )
        data = r.json()
        cash = data["player"]["cash"]

        assert_true(cash >= -100_000, "Player cash exploded negatively")

    print("✔ Negative cash guard OK")
