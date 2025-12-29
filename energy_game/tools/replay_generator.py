import json
from pathlib import Path

from src.core.engine import play_day
from src.core.state import GameState
from src.core.npc import NPCTrader
from src.config.portfolios import PORTFOLIOS


REPLAY_DIR = Path("tools/replays")
REPLAY_DIR.mkdir(parents=True, exist_ok=True)


def record_game(days, portfolio_key, npc_count, decisions):
    """
    decisions = [
        {"thermal": 20, "prices": [45, 50, 60]},
        ...
    ]
    """

    state = GameState()
    p = PORTFOLIOS[portfolio_key]

    state.solar_mw = p["solar"]
    state.wind_mw = p["wind"]
    state.thermal_mw = p["thermal"]

    npcs = [
        NPCTrader(f"NPC {i+1}", (p["solar"], p["wind"], p["thermal"]))
        for i in range(npc_count)
    ]

    replay = {
        "portfolio": portfolio_key,
        "npc_count": npc_count,
        "days": days,
        "turns": []
    }

    for day in range(days):
        d = decisions[day]
        result = play_day(
            state,
            npcs,
            d["prices"],
            d["thermal"]
        )

        replay["turns"].append({
            "decision": d,
            "result": result
        })

    return replay


def save_replay(replay, filename):
    path = REPLAY_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(replay, f, indent=2)
    return path


def load_replay(filename):
    path = REPLAY_DIR / filename
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
