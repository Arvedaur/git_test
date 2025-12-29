[ ] Backend başlıyor
[ ] /start endpoint OK
[ ] /step endpoint OK
[ ] Player cash exists
[ ] NPC list non-empty
[ ] Leaderboard sorted
/////
Testi calistirma
PYTHONPATH=. uvicorn src.server:app --host 127.0.0.1 --port 8000
python tests/test_game_smoke.py

tests/
├── test_smoke.py              # temel API ayakta mı
├── test_10_days.py            # 10 gün simülasyon
├── test_npc_bankruptcy.py     # NPC iflas testi
├── test_negative_cash.py      # negatif cash guard
├── test_performance.py        # 100 NPC performans
└── test_streamlit_ui.py       # Playwright UI testi