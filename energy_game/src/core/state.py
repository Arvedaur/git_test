class GameState:
    """
    Oyunun kalıcı durumu.
    UI'den tamamen bağımsızdır.
    """

    def __init__(self):
        self.day = 1
        self.cash = 0.0

        # Son gün açıklanan talep (forecast)
        self.base_demand = None

        # Oyuncu portföyü (MW)
        self.solar_mw = 0
        self.wind_mw = 0
        self.thermal_mw = 0
