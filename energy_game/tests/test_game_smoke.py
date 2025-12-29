import requests

BASE_URL = "http://127.0.0.1:8000"


def assert_true(cond, msg):
    if not cond:
        raise AssertionError(msg)


def test_backend_alive():
    r = requests.get(f"{BASE_URL}/")
    assert_true(r.status_code == 200, "Backend not reachable")
    data = r.json()
    assert_true("status" in data, "Missing status in root response")


def test_start_game():
    r = requests.post(f"{BASE_URL}/start", params={"npc_count": 3})
    assert_true(r.status_code == 200, "/start failed")

    data = r.json()
    assert_true(data["npc_count"] == 3, "NPC count mismatch")
    assert_true(len(data["npcs"]) == 3, "NPC list length mismatch")


def test_play_one_day():
    r = requests.post(
        f"{BASE_URL}/step",
        json={
            "player_prices": [50],
            "player_thermal_dispatch": 100,
        },
    )
    assert_true(r.status_code == 200, "/step failed")

    data = r.json()

    # Player checks
    player = data.get("player")
    assert_true(player is not None, "Missing player data")
    assert_true(isinstance(player["cash"], (int, float)), "Player cash invalid")

    # NPC checks
    npcs = data.get("npcs")
    assert_true(isinstance(npcs, list) and len(npcs) > 0, "NPC list invalid")

    for npc in npcs:
        assert_true("name" in npc, "NPC missing name")
        assert_true(isinstance(npc["cash"], (int, float)), "NPC cash invalid")

    # Leaderboard
    leaderboard = data.get("leaderboard")
    assert_true(isinstance(leaderboard, list), "Leaderboard missing")

    cash_values = [row["cash"] for row in leaderboard]
    assert_true(
        cash_values == sorted(cash_values, reverse=True),
        "Leaderboard not sorted by cash desc",
    )
