from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from random import randint
from src.core.engine import GameEngine
from src.core.state import GameState
from src.core.npc import NPCTrader
from src.shared.config import DEFAULT_CONFIG

# -------------------------------------------------
# FastAPI App
# -------------------------------------------------

app = FastAPI(
    title="Energy Game API",
    description="Turn-based energy market simulation",
    version="0.1.0",
)

# -------------------------------------------------
# Game Initialization (GLOBAL INSTANCE)
# -------------------------------------------------

state = GameState()


npcs = [
    NPCTrader("npc_1", (80, 120, 150)),
    NPCTrader("npc_2", (60, 140, 180)),
]


engine = GameEngine(
    config=DEFAULT_CONFIG,
    state=state,
    npcs=npcs,
)

# -------------------------------------------------
# API Schemas
# -------------------------------------------------

class StepAction(BaseModel):
    player_prices: List[float] = [50]
    player_thermal_dispatch: float = 0


# -------------------------------------------------
# Routes
# -------------------------------------------------

@app.get("/")
def root():
    return {
        "status": "Energy Game API running",
        "day": engine.state.day,
        "cash": engine.state.cash,
    }


@app.get("/state")
def get_state():
    """
    Anlık oyun durumu
    """
    return engine.snapshot()


@app.post("/step")
def step(action: StepAction):
    """
    Oyunda 1 gün ilerletir
    """
    report = engine.step(action.dict())
    return report
@app.post("/start")
def start_game(npc_count: int = 2):
    global engine

    npcs = [
        NPCTrader(
            name=f"npc_{i+1}",
            portfolio=(
                randint(50, 120),
                randint(80, 160),
                randint(100, 220),
            ),
        )
        for i in range(npc_count)
    ]

    engine = GameEngine(
        config=DEFAULT_CONFIG,
        state=GameState(),
        npcs=npcs,
    )

    return {
        "status": "game_started",
        "npc_count": npc_count,
        "npcs": [npc.snapshot() for npc in npcs],
    }