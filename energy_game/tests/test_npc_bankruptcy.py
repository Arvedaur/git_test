import requests
from common import BASE_URL, assert_true

def test_npc_bankruptcy():
    requests.post(f"{BASE_URL}/start", params={"npc_count": 5})

    bankrupt_found = False

    for _ in range(15):
        r = requests.post(
            f"{BASE_URL}/step",
            json={"player_prices": [30], "player_thermal_dispatch": 0},
        )
        data = r.json()

        for npc in data["npcs"]:
            if npc["cash"] < 0:
                bankrupt_found = True

    assert_true(bankrupt_found, "No NPC went bankrupt after stress test")
    print("✔ NPC bankruptcy detected")
