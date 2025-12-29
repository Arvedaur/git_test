from .strategies import RandomStrategy

class NPCTrader:
    def __init__(self, name, portfolio, cash=100_000, strategy=None):
        self.name = name
        self.solar_mw, self.wind_mw, self.thermal_mw = portfolio
        self.cash = cash
        self.strategy = strategy or RandomStrategy()

    def choose_price(self, player_prices):
        return self.strategy.choose_price(player_prices)

    def thermal_dispatch(self):
        return self.strategy.thermal_dispatch(self.thermal_mw)

    def snapshot(self):
        return {
            "name": self.name,
            "cash": round(self.cash, 1),
            "strategy": getattr(self.strategy, "name", "unknown"),
            "solar_mw": self.solar_mw,
            "wind_mw": self.wind_mw,
            "thermal_mw": self.thermal_mw,
        }
