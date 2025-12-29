import streamlit as st
import pandas as pd
import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(__file__, "../../../.."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
    
from src.core.state import GameState
from src.core.engine import play_day
from src.core.npc import NPCTrader

from src.config.portfolios import PORTFOLIOS
from src.config.defaults import DEFAULT_PRICES, DEFAULT_NPC_COUNT
from src.tutorial.tutorial import show_tutorial

import os
import streamlit as st
import requests
from src.core.engine import GameEngine
from src.shared.config import DEFAULT_CONFIG

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Energy Market Simulator",
    layout="wide"
)

# -------------------------------------------------
# Sidebar – Tutorial
# -------------------------------------------------
with st.sidebar:
    st.header("📘 Tutorial")
    if st.button("Tutorial'ı Göster"):
        show_tutorial()

# -------------------------------------------------
# Session State Init
# -------------------------------------------------
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.state = None
    st.session_state.npcs = []

# --- History for charts ---
if "history" not in st.session_state:
    st.session_state.history = {
        "day": [],
        "cash": [],
        "curtailment": [],
        "solar": [],
        "wind": [],
        "thermal": [],
        "price": [],
        "real_demand": []
    }

# -------------------------------------------------
# Game Setup
# -------------------------------------------------
st.title("⚡ Energy Market Simulator")

if not st.session_state.started:
    st.subheader("🔧 Game Setup")

    portfolio_key = st.selectbox(
        "Portföy Seç",
        list(PORTFOLIOS.keys()),
        format_func=lambda k: (
            f"{k} – {PORTFOLIOS[k]['name']} | "
            f"Güneş {PORTFOLIOS[k]['solar']} | "
            f"Rüzgar {PORTFOLIOS[k]['wind']} | "
            f"Termik {PORTFOLIOS[k]['thermal']}"
        )
    )

    npc_count = st.slider(
        "NPC Sayısı",
        1,
        4,
        DEFAULT_NPC_COUNT
    )

    if st.button("🚀 Oyunu Başlat"):
        state = GameState()
        p = PORTFOLIOS[portfolio_key]

        state.solar_mw = p["solar"]
        state.wind_mw = p["wind"]
        state.thermal_mw = p["thermal"]

        npcs = [
            NPCTrader(
                f"NPC {i+1}",
                (p["solar"], p["wind"], p["thermal"])
            )
            for i in range(npc_count)
        ]

        st.session_state.state = state
        st.session_state.npcs = npcs
        st.session_state.started = True

        # reset history on new game
        st.session_state.history = {
            "day": [],
            "cash": [],
            "curtailment": [],
            "solar": [],
            "wind": [],
            "thermal": [],
            "price": [],
            "real_demand": []
        }

        st.rerun()

# -------------------------------------------------
# Game Loop
# -------------------------------------------------
else:
    state = st.session_state.state
    npcs = st.session_state.npcs

    st.subheader(f"📅 Gün {state.day}")

    # -----------------------------
    # Player Inputs
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        thermal = st.slider(
            "🔥 Termik Dispatch (MW)",
            0.0,
            float(state.thermal_mw),
            step=1.0
        )

    with col2:
        price_input = st.text_input(
            "💰 3 Fiyat Teklifi (örn: 45 50 60)",
            " ".join(map(str, DEFAULT_PRICES))
        )

    try:
        prices = list(map(float, price_input.split()))
        assert len(prices) == 3
    except Exception:
        st.error("Lütfen 3 adet sayısal fiyat giriniz (örn: 45 50 60)")
        st.stop()

    # -----------------------------
    # Play Day
    # -----------------------------
    if st.button("▶️ Günü Oyna"):
        result = play_day(
            state=state,
            npcs=npcs,
            player_prices=prices,
            player_thermal_dispatch=thermal
        )

        # --- Save history for charts ---
        h = st.session_state.history
        h["day"].append(result["day"])
        h["cash"].append(result["cash"])
        h["curtailment"].append(result["curtailment"])
        h["solar"].append(result["solar"])
        h["wind"].append(result["wind"])
        h["thermal"].append(result["thermal"])
        h["price"].append(result["price"])
        h["real_demand"].append(result["real_demand"])

        # -----------------------------
        # Day Results
        # -----------------------------
        st.success("Gün tamamlandı")

        r1, r2, r3 = st.columns(3)

        r1.metric("Talep", f"{result['base_demand']} MWh")
        r1.metric("Gerçek Talep", f"{result['real_demand']} MWh")
        r1.metric("Fiyat", f"{result['price']} €/MWh")

        r2.metric("Güneş", f"{result['solar']} MWh")
        r2.metric("Rüzgar", f"{result['wind']} MWh")
        r2.metric("Termik", f"{result['thermal']} MWh")

        r3.metric("Satılan", f"{result['sold']} MWh")
        r3.metric("Curtailment", f"{result['curtailment']} MWh")
        r3.metric("Toplam Nakit", f"{result['cash']} €")

    # -------------------------------------------------
    # Performance Dashboard
    # -------------------------------------------------
    st.divider()
    st.subheader("📊 Performance Dashboard")

    df = pd.DataFrame(st.session_state.history)

    if not df.empty:
        g1, g2 = st.columns(2)

        with g1:
            st.write("💰 Cash Over Time")
            st.line_chart(df.set_index("day")["cash"])

        with g2:
            st.write("⚡ Curtailment (MWh)")
            st.bar_chart(df.set_index("day")["curtailment"])

        st.divider()

        st.write("🔌 Production Mix")
        prod_df = df[["day", "solar", "wind", "thermal"]].set_index("day")
        st.area_chart(prod_df)

        st.divider()

        st.write("💲 Price vs Real Demand")
        price_df = df[["day", "price", "real_demand"]].set_index("day")
        st.line_chart(price_df)

    # -------------------------------------------------
    # Reset Game
    # -------------------------------------------------
    st.divider()
    if st.button("🔄 Oyunu Sıfırla"):
        st.session_state.started = False
        st.session_state.state = None
        st.session_state.npcs = []
        st.session_state.history = {
            "day": [],
            "cash": [],
            "curtailment": [],
            "solar": [],
            "wind": [],
            "thermal": [],
            "price": [],
            "real_demand": []
        }
        st.rerun()



USE_API = os.getenv("USE_API", "0") == "1"

if USE_API:
    API_URL = os.getenv("API_URL", "http://localhost:8000")

    def get_state():
        return requests.get(f"{API_URL}/state").json()

    def step(action):
        return requests.post(f"{API_URL}/step", json=action).json()
else:
    engine = GameEngine(DEFAULT_CONFIG)

    def get_state():
        return engine.snapshot()

    def step(action):
        return engine.step({"action": "next"})
