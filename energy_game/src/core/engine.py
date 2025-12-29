from .rules import (
    generate_demand,
    real_demand,
    solar_production,
    wind_production,
    maintenance_multiplier,
    softmax_shares,
)

# -----------------------------
# Cost Constants
# -----------------------------
SOLAR_MAINT = 300
WIND_MAINT = 400
THERMAL_MAINT = 600
THERMAL_FUEL_COST = 25  # €/MWh


def _fixed_cost(mult):
    return (SOLAR_MAINT + WIND_MAINT + THERMAL_MAINT) * mult


def play_day(state, npcs, player_prices, player_thermal_dispatch):
    """
    Günlük simülasyon.
    Dönen yapı:
    {
      "player": {...},
      "npcs": [...],
      "leaderboard": [...]
    }
    """

    # --------------------------------------------------
    # 1) Demand
    # --------------------------------------------------
    state.base_demand = generate_demand(state.base_demand)

    # --------------------------------------------------
    # 2) Player production
    # --------------------------------------------------
    p_solar = solar_production(state.solar_mw)
    p_wind = wind_production(state.wind_mw)
    p_thermal = min(player_thermal_dispatch, state.thermal_mw)
    p_prod = p_solar + p_wind + p_thermal

    # --------------------------------------------------
    # 3) Prices
    # --------------------------------------------------
    p_price = min(player_prices) if player_prices else 50
    npc_prices = [npc.choose_price(player_prices) for npc in npcs]
    prices = [p_price] + npc_prices

    ref_price = min(prices)

    # --------------------------------------------------
    # 4) Shares
    # --------------------------------------------------
    rd = real_demand(state.base_demand, ref_price)
    shares = softmax_shares(prices)

    # --------------------------------------------------
    # 5) Player sales
    # --------------------------------------------------
    p_target = rd * shares[0]
    p_sold = min(p_target, p_prod)
    p_curtail = p_prod - p_sold
    p_revenue = p_sold * p_price

    mult = maintenance_multiplier(state.base_demand, len(prices))
    p_fixed = _fixed_cost(mult)
    p_fuel = p_thermal * THERMAL_FUEL_COST
    p_cost = p_fixed + p_fuel

    state.cash += p_revenue - p_cost
    state.day += 1

    # --------------------------------------------------
    # 6) NPCs
    # --------------------------------------------------
    npc_reports = []
    leaderboard = []

    for i, npc in enumerate(npcs):
        npc_price = prices[i + 1]
        npc_share = shares[i + 1]
        npc_target = rd * npc_share

        n_solar = solar_production(npc.solar_mw)
        n_wind = wind_production(npc.wind_mw)
        n_thermal = min(npc.thermal_dispatch(), npc.thermal_mw)
        n_prod = n_solar + n_wind + n_thermal

        n_sold = min(npc_target, n_prod)
        n_curtail = n_prod - n_sold
        n_revenue = n_sold * npc_price

        n_fixed = _fixed_cost(mult)
        n_fuel = n_thermal * THERMAL_FUEL_COST
        n_cost = n_fixed + n_fuel

        if not hasattr(npc, "cash"):
            npc.cash = 0.0
        npc.cash += n_revenue - n_cost

        npc_reports.append({
            "name": npc.name,
            "price": npc_price,
            "sold": round(n_sold, 1),
            "revenue": round(n_revenue, 1),
            "cost": round(n_cost, 1),
            "cash": round(npc.cash, 1),
        })

        leaderboard.append({
            "name": npc.name,
            "cash": npc.cash,
            "revenue": n_revenue,
            "cost": n_cost,
            "sold": n_sold,
        })

    # --------------------------------------------------
    # 7) Player report + leaderboard
    # --------------------------------------------------
    leaderboard.append({
        "name": "player",
        "cash": state.cash,
        "revenue": p_revenue,
        "cost": p_cost,
        "sold": p_sold,
    })

    leaderboard = sorted(
        leaderboard,
        key=lambda x: (x["cash"], x["revenue"]),
        reverse=True,
    )

    for i, row in enumerate(leaderboard, start=1):
        row["rank"] = i
        for k in ["cash", "revenue", "cost", "sold"]:
            row[k] = round(float(row[k]), 1)

    return {
        "player": {
            "day": state.day - 1,
            "cash": round(state.cash, 1),
            "revenue": round(p_revenue, 1),
            "cost": round(p_cost, 1),
            "sold": round(p_sold, 1),
            "curtailment": round(p_curtail, 1),
        },
        "npcs": npc_reports,
        "leaderboard": leaderboard,
    }


# ==========================================================
# GAME ENGINE WRAPPER
# ==========================================================
class GameEngine:
    def __init__(self, config, state, npcs):
        self.config = config
        self.state = state
        self.npcs = npcs

    def snapshot(self):
        return {
            "day": self.state.day,
            "cash": round(self.state.cash, 1),
            "npcs": [
                {"name": n.name, "cash": round(float(getattr(n, "cash", 0.0)), 1)}
                for n in self.npcs
            ],
        }

    def step(self, action: dict):
        return play_day(
            state=self.state,
            npcs=self.npcs,
            player_prices=action.get("player_prices", [50]),
            player_thermal_dispatch=action.get("player_thermal_dispatch", 0),
        )
