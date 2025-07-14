from utils.load_data import load_categories_from_json
from pathlib import Path
from src.models.product import Product
from src.models.smartphone import Smartphone
from src.models.lawngrass import LawnGrass
from src.models.category import Category

def main():
    # Создаем обычные продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    # Создаем смартфон
    smartphone = Smartphone(
        "Xiaomi 13T", "Flagship", 70000, 10,
        95.5, "13T Pro", 256, "Blue"
    )

    # Создаем категории
    electronics = Category("Электроника", "Техника", [product1, product2, smartphone])

    print("Категория:", electronics.name)
    print("Описание:", electronics.description)
    print("Количество продуктов:", len(electronics.products))


if __name__ == '__main__':
    main()
