from utils.load_data import load_categories_from_json
from models.product import Product
from models.category import Category
from pathlib import Path


def main():
    # 1. Ручное создание объектов
    print("=== РУЧНОЕ СОЗДАНИЕ ОБЪЕКТОВ ===")
    manual_demo()

    # 2. Загрузка из JSON
    print("\n=== ЗАГРУЗКА ИЗ JSON ===")
    json_path = Path(__file__).parent.parent / "data" / "products.json"
    json_demo(json_path)


def manual_demo():
    """Демонстрация ручного создания объектов"""
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создание товаров
    products = [
        Product("Xiaomi", "Смартфон", 25000.0, 10),
        Product("Samsung", "Планшет", 45000.0, 5)
    ]

    # Создание категории
    category = Category("Электроника", "Техника", products)

    # Вывод информации
    print(f"Создана категория: {category}")
    print(f"Товары: {category.products}")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


def json_demo(json_path: Path):
    """Демонстрация загрузки из JSON"""
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Загрузка данных
    categories = load_categories_from_json(json_path)

    # Вывод информации
    for category in categories:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Товары ({len(category.products)}):")
        for product in category.products:
            print(f"  - {product.name}: {product.price} руб. ({product.quantity} шт.)")

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
