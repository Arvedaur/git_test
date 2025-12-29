import requests, time
from common import BASE_URL, assert_true

def test_performance_100_npc():
    r = requests.post(f"{BASE_URL}/start", params={"npc_count": 100})
    assert_true(r.status_code == 200, "Failed to start with 100 NPCs")

    start = time.time()

    r = requests.post(
        f"{BASE_URL}/step",
        json={"player_prices": [50], "player_thermal_dispatch": 100},
    )

    elapsed = time.time() - start

    assert_true(r.status_code == 200, "Step failed with 100 NPCs")
    assert_true(elapsed < 2.0, f"Performance too slow: {elapsed:.2f}s")

    print(f"✔ Performance OK: {elapsed:.2f}s for 100 NPCs")
