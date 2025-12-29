from src.core.state import GameState
from src.core.engine import play_day
from src.core.npc import NPCTrader

def test_play_day_runs():
    state = GameState()
    state.solar_mw = 80
    state.wind_mw = 80
    state.thermal_mw = 40

    npcs = [NPCTrader("NPC1", (80, 80, 40))]

    result = play_day(
        state,
        npcs,
        player_prices=[45, 50, 60],
        player_thermal_dispatch=20
    )

    assert "cash" in result
    assert state.day == 2
