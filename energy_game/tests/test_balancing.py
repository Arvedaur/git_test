from simulations.monte_carlo import run_monte_carlo

def test_game_not_always_losing():
    result = run_monte_carlo(
        runs=50,
        days=3,
        portfolio_key="A",
        npc_count=4
    )

    # Oyunun en azından BAZEN kâr üretmesi gerekir
    assert result["profitable_pct"] > 0
