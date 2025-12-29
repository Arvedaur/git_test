from rules import *

SOLAR_MAINT = 300
WIND_MAINT = 400
THERMAL_MAINT = 600
THERMAL_FUEL = 25

def play_day(state, npcs, player_prices, player_thermal):
    # Demand
    state.base_demand = generate_demand(state.base_demand)

    # Production
    solar = solar_production(state.solar_mw)
    wind = wind_production(state.wind_mw)
    thermal = min(player_thermal, state.thermal_mw)
    production = solar + wind + thermal

    # Offers
    npc_prices = [npc.choose_price(player_prices) for npc in npcs]
    prices = [min(player_prices)] + npc_prices
    ref_price = min(prices)

    # Demand & shares
    rd = real_demand(state.base_demand, ref_price)
    shares = softmax_shares(prices)

    player_target = rd * shares[0]
    sold = min(player_target, production)
    curtailment = production - sold

    # Revenue
    revenue = sold * min(player_prices)

    # Costs
    mult = maintenance_multiplier(state.base_demand, len(prices))
    fixed_cost = (SOLAR_MAINT + WIND_MAINT + THERMAL_MAINT) * mult
    fuel_cost = thermal * THERMAL_FUEL
    cost = fixed_cost + fuel_cost

    state.cash += revenue - cost
    state.day += 1

    return {
        "demand": round(state.base_demand, 1),
        "real_demand": round(rd, 1),
        "solar": round(solar, 1),
        "wind": round(wind, 1),
        "thermal": round(thermal, 1),
        "sold": round(sold, 1),
        "curtailment": round(curtailment, 1),
        "price": min(player_prices),
        "revenue": round(revenue, 1),
        "cost": round(cost, 1),
        "cash": round(state.cash, 1),
    }
