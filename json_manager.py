import json
import os
from pathlib import Path


class KingdomJSON:
    @staticmethod
    def save_kingdom(name, data):
        """Сохраняет данные королевства в JSON-файл"""
        filename = f"saves/kingdom_{name}.json"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False

    @staticmethod
    def load_kingdom(name):
        """Загружает данные королевства из JSON-файла"""
        filename = f"saves/kingdom_{name}.json"
        if not os.path.exists(filename):
            return None

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError as e:
            print(f"Ошибка чтения JSON: {e}")
            return None
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
            return None

    @staticmethod
    def list_kingdoms():
        """Возвращает список доступных королевств (по файлам)"""
        kingdoms = []
        for file in Path(".").glob("kingdom_*.json"):
            # Извлекаем имя из имени файла
            name = file.name.replace("kingdom_", "").replace(".json", "")
            kingdoms.append(name)
        return kingdoms
