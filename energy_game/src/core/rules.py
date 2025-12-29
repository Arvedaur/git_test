import random
import math

# -----------------------------
# Demand
# -----------------------------

def generate_demand(previous=None):
    """
    Gün başında açıklanan piyasa talebi (MWh).
    """
    if previous is None:
        return random.randint(160, 220)
    return max(80, previous + random.randint(-20, 20))


def real_demand(base_demand, ref_price):
    """
    Fiyat elastikiyeti.
    Fiyat yükseldikçe gerçek talep düşer.
    """
    return max(base_demand * (1.25 - ref_price / 100), 0.0)

# -----------------------------
# Production
# -----------------------------

def solar_production(capacity):
    return capacity * random.uniform(0.30, 0.70)


def wind_production(capacity):
    return capacity * random.uniform(0.25, 0.75)

# -----------------------------
# Cost Scaling
# -----------------------------

def maintenance_multiplier(base_demand, actor_count):
    """
    Talep / aktör oranına göre sabit maliyet skalası.
    60 MWh/aktör => 1.0x
    Clamp: 0.60x – 1.20x
    """
    demand_per_actor = base_demand / actor_count
    return max(0.60, min(1.20, demand_per_actor / 60.0))

# -----------------------------
# Market Share
# -----------------------------

def softmax_shares(prices, k=0.12):
    """
    Fiyat bazlı satış payı.
    Daha ucuz fiyat => daha yüksek pay.
    """
    exp = [math.exp(-k * p) for p in prices]
    total = sum(exp)
    return [e / total for e in exp]
