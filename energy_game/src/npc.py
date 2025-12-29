import random

class NPCTrader:
    def __init__(self, name, portfolio):
        self.name = name
        self.solar, self.wind, self.thermal = portfolio

    def thermal_dispatch(self):
        return random.uniform(0.4, 0.9) * self.thermal

    def choose_price(self, player_prices):
        return min(player_prices) + random.randint(-3, 4)
