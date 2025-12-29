"""
Sabit oyun parametreleri.
Balancing burada yapılır.
"""

# --- Maintenance (€/day) ---
SOLAR_MAINT = 300
WIND_MAINT = 400
THERMAL_MAINT = 600

# --- Thermal ---
THERMAL_FUEL_COST = 25  # €/MWh

# --- Demand ---
DEMAND_MIN = 160
DEMAND_MAX = 220
DEMAND_DRIFT = 20

# --- Production Variance ---
SOLAR_MIN = 0.30
SOLAR_MAX = 0.70
WIND_MIN = 0.25
WIND_MAX = 0.75

# --- Market Share ---
SOFTMAX_K = 0.12

# --- Cost Scaling ---
BASE_DEMAND_PER_ACTOR = 60
MIN_COST_MULTIPLIER = 0.60
MAX_COST_MULTIPLIER = 1.20
