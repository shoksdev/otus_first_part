import csv
from typing import List, Dict


def read_csv(file_path: str) -> List[Dict]:
    """Читает CSV как список словарей"""
    with open(file_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_csv(file_path: str, data: List[Dict], fieldnames: List[str]) -> None:
    """Записывает список словарей в CSV"""
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
