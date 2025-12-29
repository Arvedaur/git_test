from src.core.rules import real_demand, maintenance_multiplier

def test_real_demand_decreases_with_price():
    base = 200
    low_price = real_demand(base, 40)
    high_price = real_demand(base, 80)
    assert low_price > high_price


def test_maintenance_multiplier_bounds():
    m_low = maintenance_multiplier(100, 5)
    m_high = maintenance_multiplier(500, 1)

    assert 0.60 <= m_low <= 1.20
    assert 0.60 <= m_high <= 1.20
