import json
from pathlib import Path
from typing import List
from src.models.product import Product
from src.models.category import Category


def load_categories_from_json(file_path: str | Path) -> List[Category]:
    """Загружает данные из JSON с проверкой формата"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Ошибка загрузки JSON: {str(e)}")

    if not isinstance(data, list):
        raise ValueError("Неверный формат JSON: ожидается список категорий")

    categories = []
    for category_data in data:
        try:
            products = [
                Product(
                    name=str(product['name']),
                    description=str(product['description']),
                    price=float(product['price']),
                    quantity=int(product['quantity'])
                )
                for product in category_data['products']
            ]
            categories.append(
                Category(
                    name=str(category_data['name']),
                    description=str(category_data['description']),
                    products=products
                )
            )
        except (KeyError, ValueError) as e:
            raise ValueError(f"Ошибка в структуре данных: {str(e)}")

    return categories
