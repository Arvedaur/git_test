#!/bin/bash
set -e

# -------------------------------------------------
# Resolve project root (script location -> parent)
# -------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

export PYTHONPATH="$PROJECT_ROOT"

echo "▶ Project root: $PROJECT_ROOT"

# -------------------------------------------------
# Backend
# -------------------------------------------------
if lsof -i :8000 >/dev/null 2>&1; then
  echo "🟡 Backend already running on port 8000"
  SERVER_PID=""
else
  echo "▶ Starting backend..."
  cd "$PROJECT_ROOT"
  uvicorn src.server:app --host 127.0.0.1 --port 8000 &
  SERVER_PID=$!
  sleep 3
fi

# -------------------------------------------------
# Streamlit
# -------------------------------------------------
echo "▶ Starting Streamlit..."
cd "$PROJECT_ROOT"
streamlit run src/ui/streamlit/app.py --server.headless true &
UI_PID=$!
sleep 6

# -------------------------------------------------
# Tests
# -------------------------------------------------
echo "▶ Running tests..."
cd "$PROJECT_ROOT"
python tests/test_10_days.py
python tests/test_npc_bankruptcy.py
python tests/test_negative_cash.py
python tests/test_performance.py
python tests/test_streamlit_ui.py

echo "✅ ALL GAME TESTS PASSED"

# -------------------------------------------------
# Cleanup
# -------------------------------------------------
echo "▶ Stopping services..."
if [ -n "$SERVER_PID" ]; then
  kill $SERVER_PID || true
fi
kill $UI_PID || true

python tests/report_runner.py
echo "Report: $PROJECT_ROOT/reports/report.html"

