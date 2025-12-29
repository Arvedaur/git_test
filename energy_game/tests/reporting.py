import json, time, traceback
from dataclasses import dataclass, asdict
from typing import Any, Callable, Dict, List, Optional

@dataclass
class TestResult:
    name: str
    ok: bool
    duration_s: float
    details: Dict[str, Any]
    error: Optional[str] = None

def run_test(name: str, fn: Callable[[], Dict[str, Any] | None]) -> TestResult:
    t0 = time.time()
    try:
        details = fn() or {}
        return TestResult(name=name, ok=True, duration_s=time.time()-t0, details=details)
    except Exception:
        return TestResult(
            name=name,
            ok=False,
            duration_s=time.time()-t0,
            details={},
            error=traceback.format_exc(),
        )

def write_json(path: str, results: List[TestResult]) -> None:
    payload = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total": len(results),
            "passed": sum(r.ok for r in results),
            "failed": sum(not r.ok for r in results),
            "duration_s": round(sum(r.duration_s for r in results), 3),
        },
        "results": [asdict(r) for r in results],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

def write_html(path: str, json_payload: Dict[str, Any]) -> None:
    s = json_payload["summary"]
    rows = []
    for r in json_payload["results"]:
        status = "PASS" if r["ok"] else "FAIL"
        rows.append(f"""
          <tr>
            <td>{r['name']}</td>
            <td class="{status.lower()}">{status}</td>
            <td>{r['duration_s']:.3f}</td>
            <td><pre>{json.dumps(r.get('details', {}), ensure_ascii=False, indent=2)}</pre></td>
          </tr>
        """)
    html = f"""
    <html><head>
      <meta charset="utf-8" />
      <title>Energy Game – Test Report</title>
      <style>
        body {{ font-family: Arial, sans-serif; margin: 24px; }}
        .pass {{ color: #0a7a0a; font-weight: bold; }}
        .fail {{ color: #b00020; font-weight: bold; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; vertical-align: top; }}
        th {{ background: #f6f6f6; }}
        pre {{ margin: 0; white-space: pre-wrap; }}
      </style>
    </head><body>
      <h1>Energy Game – Health Dashboard</h1>
      <p><b>Generated:</b> {json_payload['generated_at']}</p>
      <p><b>Summary:</b> total={s['total']} passed={s['passed']} failed={s['failed']} duration={s['duration_s']}s</p>
      <table>
        <thead>
          <tr><th>Test</th><th>Status</th><th>Duration (s)</th><th>Details</th></tr>
        </thead>
        <tbody>
          {''.join(rows)}
        </tbody>
      </table>
    </body></html>
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
