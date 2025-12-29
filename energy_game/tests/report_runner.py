import os, json
from reporting import run_test, write_json, write_html

# Burada test fonksiyonlarını “import edip” çağıracağız.
from test_10_days import test_10_days_simulation
from test_npc_bankruptcy import test_npc_bankruptcy
from test_negative_cash import test_negative_cash_guard
from test_performance import test_performance_100_npc
from test_streamlit_ui import test_streamlit_ui

def _wrap(fn):
    # test fonksiyonların print edebilir; biz details döndürmeyi teşvik ediyoruz.
    # Şimdilik None dönse bile problem yok.
    return fn

def main():
    os.makedirs("reports", exist_ok=True)

    results = [
        run_test("10-day simulation", _wrap(test_10_days_simulation)),
        run_test("npc bankruptcy", _wrap(test_npc_bankruptcy)),
        run_test("negative cash guard", _wrap(test_negative_cash_guard)),
        run_test("performance 100 npc", _wrap(test_performance_100_npc)),
        run_test("streamlit ui", _wrap(test_streamlit_ui)),
    ]

    json_path = "reports/report.json"
    html_path = "reports/report.html"

    write_json(json_path, results)

    with open(json_path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    write_html(html_path, payload)

    failed = [r for r in results if not r.ok]
    if failed:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
