import csv
import json
from datetime import datetime
from pathlib import Path


RESULTS_DIR = Path("simulations/results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def export_to_csv(data: list[dict], filename: str | None = None):
    """
    Liste halinde dict alır ve CSV yazar.
    """
    if not data:
        raise ValueError("Export edilecek veri yok")

    if filename is None:
        filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    path = RESULTS_DIR / filename

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    return path


def export_to_json(data: list[dict], filename: str | None = None):
    """
    Liste halinde dict alır ve JSON yazar.
    """
    if filename is None:
        filename = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    path = RESULTS_DIR / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return path
