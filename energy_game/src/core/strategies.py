import random

class BaseStrategy:
    name = "base"
    def choose_price(self, player_prices):
        return min(player_prices) if player_prices else 50
    def thermal_dispatch(self, thermal_mw):
        return 0.0

class AggressiveStrategy(BaseStrategy):
    name = "aggressive"
    def choose_price(self, player_prices):
        base = min(player_prices) if player_prices else 50
        return base - random.randint(1, 4)  # daha ucuz -> daha fazla pay
    def thermal_dispatch(self, thermal_mw):
        return random.uniform(0.6, 0.95) * thermal_mw

class ConservativeStrategy(BaseStrategy):
    name = "conservative"
    def choose_price(self, player_prices):
        base = min(player_prices) if player_prices else 50
        return base + random.randint(0, 5)  # daha pahalı -> daha az pay, daha yüksek margin denemesi
    def thermal_dispatch(self, thermal_mw):
        return random.uniform(0.2, 0.6) * thermal_mw

class RandomStrategy(BaseStrategy):
    name = "random"
    def choose_price(self, player_prices):
        base = min(player_prices) if player_prices else 50
        return base + random.randint(-6, 6)
    def thermal_dispatch(self, thermal_mw):
        return random.uniform(0.0, 1.0) * thermal_mw
