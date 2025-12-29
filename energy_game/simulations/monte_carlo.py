import random, statistics
import requests

BASE_URL = "http://127.0.0.1:8000"

def run_episode(days=30, npc_count=5):
    requests.post(f"{BASE_URL}/start", params={"npc_count": npc_count})

    cash_series = []
    curtail_series = []

    for _ in range(days):
        # basit politika: fiyatı hafif rastgeleleştir, thermal orta seviyede
        price = random.randint(40, 60)
        thermal = random.randint(60, 160)

        r = requests.post(f"{BASE_URL}/step", json={
            "player_prices": [price],
            "player_thermal_dispatch": thermal
        })
        data = r.json()
        cash_series.append(data["player"]["cash"])
        curtail_series.append(data["player"].get("curtailment", 0.0))

    final_cash = cash_series[-1]
    bankrupt = final_cash < 0
    return {
        "final_cash": final_cash,
        "bankrupt": bankrupt,
        "cash_mean": statistics.mean(cash_series),
        "cash_stdev": statistics.pstdev(cash_series),
        "curtail_mean": statistics.mean(curtail_series),
    }

def monte_carlo(runs=200, days=30, npc_count=5):
    results = [run_episode(days=days, npc_count=npc_count) for _ in range(runs)]
    bankrupt_rate = sum(r["bankrupt"] for r in results) / runs
    return {
        "runs": runs,
        "days": days,
        "npc_count": npc_count,
        "bankrupt_rate": round(bankrupt_rate, 3),
        "final_cash_avg": round(statistics.mean(r["final_cash"] for r in results), 1),
        "final_cash_p50": round(statistics.median(r["final_cash"] for r in results), 1),
        "curtail_mean_avg": round(statistics.mean(r["curtail_mean"] for r in results), 2),
    }

if __name__ == "__main__":
    print(monte_carlo(runs=200, days=30, npc_count=5))
