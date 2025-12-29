class GameState:
    def __init__(self):
        self.day = 1
        self.cash = 0.0
        self.risk = 0.10
        self.base_demand = None

        # Portfolio (MW)
        self.solar_mw = 0
        self.wind_mw = 0
        self.thermal_mw = 0
