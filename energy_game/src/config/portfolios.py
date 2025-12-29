"""
Oyunun başında seçilen üretim portföyleri (MW).
Bu dosya sadece konfigürasyon içerir.
"""

PORTFOLIOS = {
    "A": {
        "name": "Balanced Renewables",
        "solar": 80,
        "wind": 80,
        "thermal": 40,
    },
    "B": {
        "name": "Solar Heavy",
        "solar": 100,
        "wind": 60,
        "thermal": 40,
    },
    "C": {
        "name": "Wind Heavy",
        "solar": 60,
        "wind": 100,
        "thermal": 40,
    },
    "D": {
        "name": "Thermal Support",
        "solar": 80,
        "wind": 40,
        "thermal": 60,
    },
    "E": {
        "name": "Thermal Dominant",
        "solar": 40,
        "wind": 40,
        "thermal": 100,
    },
}
