import streamlit as st

from state import GameState
from npc import NPCTrader
from engine import play_day
from tutorial import show_tutorial

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Energy Market Simulator",
    layout="wide"
)

# -------------------------------
# Sidebar – Tutorial
# -------------------------------
with st.sidebar:
    st.header("📘 Tutorial")
    if st.button("Tutorial'ı Göster"):
        show_tutorial()

# -------------------------------
# Session State Init
# -------------------------------
if "state" not in st.session_state:
    st.session_state.state = None
    st.session_state.npcs = []
    st.session_state.started = False

# -------------------------------
# Portfolio Definitions
# -------------------------------
PORTFOLIOS = {
    "A": (80, 80, 40),
    "B": (100, 60, 40),
    "C": (60, 100, 40),
    "D": (80, 40, 60),
    "E": (40, 40, 100),
}

# -------------------------------
# GAME SETUP
# -------------------------------
st.title("⚡ Energy Market Simulator")

if not st.session_state.started:
    st.subheader("🔧 Oyun Ayarları")

    portfolio_key = st.selectbox(
        "Portföy Seç (1 kere)",
        list(PORTFOLIOS.keys()),
        format_func=lambda k: f"{k} → Güneş {PORTFOLIOS[k][0]} | "
                              f"Rüzgar {PORTFOLIOS[k][1]} | "
                              f"Termik {PORTFOLIOS[k][2]}"
    )

    npc_count = st.slider("NPC Sayısı", 1, 4, 2)

    if st.button("🚀 Oyunu Başlat"):
        state = GameState()
        solar, wind, thermal = PORTFOLIOS[portfolio_key]
        state.solar_mw = solar
        state.wind_mw = wind
        state.thermal_mw = thermal

        npcs = [
            NPCTrader(f"NPC {i+1}", PORTFOLIOS[portfolio_key])
            for i in range(npc_count)
        ]

        st.session_state.state = state
        st.session_state.npcs = npcs
        st.session_state.started = True

        st.experimental_rerun()

# -------------------------------
# GAME LOOP UI
# -------------------------------
else:
    state = st.session_state.state
    npcs = st.session_state.npcs

    st.subheader(f"📅 Gün {state.day}")

    # ---------------------------
    # Player Inputs
    # ---------------------------
    col1, col2 = st.columns(2)

    with col1:
        thermal = st.slider(
            "🔥 Termik Dispatch (MW)",
            0.0,
            float(state.thermal_mw),
            step=1.0
        )

    with col2:
        prices = st.text_input(
            "💰 3 Fiyat Teklifi (örn: 45 50 60)",
            value="45 50 60"
        )

    prices = [float(p) for p in prices.split()]

    # ---------------------------
    # Play Day
    # ---------------------------
    if st.button("▶️ Günü Oyna"):
        result = play_day(
            state=state,
            npcs=npcs,
            player_prices=prices,
            player_thermal=thermal
        )

        # -----------------------
        # RESULTS
        # -----------------------
        st.success("Gün tamamlandı")

        r1, r2, r3 = st.columns(3)

        r1.metric("Talep", f"{result['demand']} MWh")
        r1.metric("Gerçek Talep", f"{result['real_demand']} MWh")
        r1.metric("Fiyat", f"{result['price']} €/MWh")

        r2.metric("Güneş", f"{result['solar']} MWh")
        r2.metric("Rüzgar", f"{result['wind']} MWh")
        r2.metric("Termik", f"{result['thermal']} MWh")

        r3.metric("Satılan", f"{result['sold']} MWh")
        r3.metric("Curtailment", f"{result['curtailment']} MWh")
        r3.metric("Nakit", f"{result['cash']} €")

        st.divider()

        st.write("### 💸 Finansal Özet")
        st.write(f"- Gelir: **{result['revenue']} €**")
        st.write(f"- Maliyet: **{result['cost']} €**")

    # ---------------------------
    # RESET
    # ---------------------------
    st.divider()
    if st.button("🔄 Oyunu Sıfırla"):
        st.session_state.started = False
        st.session_state.state = None
        st.session_state.npcs = []
        st.experimental_rerun()
