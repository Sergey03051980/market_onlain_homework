from utils.load_data import load_categories_from_json
from src.models.product import Product
from src.models.category import Category
from src.models.category_iterator import CategoryIterator
from pathlib import Path


def main():
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", 180000.0, 5, "256GB, Серый цвет, 200MP камера")
    product2 = Product("Iphone 15", 210000.0, 8, "512GB, Gray space")
    product3 = Product("Xiaomi Redmi Note 11", 31000.0, 14, "1024GB, Синий")

    print("=== ТЕСТИРОВАНИЕ ПРОДУКТОВ ===")
    # Демонстрация строкового представления продуктов
    print("\nСтроковое представление продуктов:")
    print(product1)
    print(product2)
    print(product3)

    # Создаем категорию
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print("\n=== ТЕСТИРОВАНИЕ КАТЕГОРИИ ===")
    # Демонстрация строкового представления категории
    print("\nСтроковое представление категории:")
    print(category1)

    # Демонстрация списка продуктов
    print("\nСписок продуктов в категории:")
    for product in category1:
        print(f"  - {product}")

    # Демонстрация сложения продуктов
    print("\n=== ТЕСТИРОВАНИЕ СЛОЖЕНИЯ ПРОДУКТОВ ===")
    print(f"Суммарная стоимость {product1.name} и {product2.name}: {product1 + product2} руб.")
    print(f"Суммарная стоимость {product1.name} и {product3.name}: {product1 + product3} руб.")
    print(f"Суммарная стоимость {product2.name} и {product3.name}: {product2 + product3} руб.")

    # Демонстрация общего количества товаров в категории
    print("\nОбщее количество товаров в категории:")
    print(f"Всего товаров: {sum(p.quantity for p in category1)} шт.")

    # Демонстрация работы итератора
    print("\nПеребор товаров в категории через итератор:")
    for i, product in enumerate(category1, 1):
        print(f"{i}. {product.name} - {product.price} руб. (остаток: {product.quantity} шт.)")


if __name__ == "__main__":
    main()
