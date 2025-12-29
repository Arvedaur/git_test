from simulations.monte_carlo import run_monte_carlo

SCENARIOS = [
    {"portfolio": "A", "npc": 2},
    {"portfolio": "A", "npc": 4},
    {"portfolio": "C", "npc": 4},
    {"portfolio": "E", "npc": 4},
]


def run_all_scenarios():
    results = []

    for s in SCENARIOS:
        res = run_monte_carlo(
            runs=200,
            days=3,
            portfolio_key=s["portfolio"],
            npc_count=s["npc"]
        )
        results.append(res)

    return results


if __name__ == "__main__":
    all_results = run_all_scenarios()
    for r in all_results:
        print(r)
