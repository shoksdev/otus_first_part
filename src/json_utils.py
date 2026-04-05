import json
from typing import Union


def read_json(file_path: str) -> Union[list, dict]:
    """Читает JSON файл и возвращает данные"""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(file_path: str, data: Union[list, dict]) -> None:
    """Записывает данные в JSON файл"""
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
