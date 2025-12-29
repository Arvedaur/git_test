import random
import math

# --- Production ---
def solar_production(cap):
    return cap * random.uniform(0.30, 0.70)

def wind_production(cap):
    return cap * random.uniform(0.25, 0.75)

# --- Demand ---
def generate_demand(prev=None):
    if prev is None:
        return random.randint(160, 220)
    return max(80, prev + random.randint(-20, 20))

def real_demand(base, ref_price):
    return max(base * (1.25 - ref_price / 100), 0)

# --- Cost scaling ---
def maintenance_multiplier(demand, actors):
    demand_per_actor = demand / actors
    return max(0.60, min(1.20, demand_per_actor / 60))

# --- Market share (price based) ---
def softmax_shares(prices, k=0.12):
    exp = [math.exp(-k * p) for p in prices]
    s = sum(exp)
    return [e / s for e in exp]
