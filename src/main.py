from utils.load_data import load_categories_from_json
from pathlib import Path
from src.models.product import Product
from src.models.smartphone import Smartphone
from src.models.lawngrass import LawnGrass
from src.models.category import Category
from src.models.exceptions import ZeroQuantityError

from src.models.product import Product
from src.models.smartphone import Smartphone
from src.models.lawngrass import LawnGrass
from src.models.category import Category
from src.models.exceptions import ZeroQuantityError

def main():
    # Тест обработки нулевого количества товара
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(f"Ошибка: {e}")
        print("Программа продолжает работу после обработки ошибки")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    # Создание корректных продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Smartphone("Xiaomi 13T", "Flagship", 70000, 10, "Dimensity", "13T Pro", "256GB", "Blue")
    product4 = LawnGrass("Газон Premium", "Мягкая трава", 500, 100, "Россия", "14 дней", "Зелёный")

    # Создание категории и добавление продуктов
    category1 = Category("Смартфоны", "Категория смартфонов")
    for product in [product1, product2, product3]:
        try:
            category1.add_product(product)
        except ZeroQuantityError as e:
            print(f"Ошибка добавления: {e}")

    # Тест среднего ценника (исправлено на average_price)
    print(f"\nСредняя цена в категории '{category1.name}': {category1.average_price():.2f} руб.")

    # Тест пустой категории
    category_empty = Category("Пустая категория", "Категория без продуктов")
    print(f"Средняя цена в пустой категории: {category_empty.average_price():.2f} руб.")

    # Добавление товара с нулевым количеством через метод add_product
    print("\nПопытка добавить товар с нулевым количеством:")
    try:
        category1.add_product(Product("Nokia 3310", "Легендарный", 5000, 0))
    except ZeroQuantityError as e:
        print(f"Поймано исключение: {e}")

    # Вывод информации о категории
    print(f"\nИтоговая информация о категории '{category1.name}':")
    print(f"Количество продуктов: {len(category1.products)}")
    print(f"Общая стоимость: {sum(p.price * p.quantity for p in category1.products):.2f} руб.")

if __name__ == "__main__":
    main()
