from utils.load_data import load_categories_from_json
from pathlib import Path
from src.models.product import Product
from src.models.smartphone import Smartphone
from src.models.lawngrass import LawnGrass
from src.models.category import Category


def main():
    # Создаем смартфоны
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый"
    )

    smartphone2 = Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space"
    )

    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий"
    )

    # Создаем газонную траву
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый"
    )

    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый"
    )

    # Демонстрация сложения
    try:
        smartphone_sum = smartphone1 + smartphone2
        print(f"Суммарная стоимость смартфонов: {smartphone_sum}")

        grass_sum = grass1 + grass2
        print(f"Суммарная стоимость газонной травы: {grass_sum}")

        invalid_sum = smartphone1 + grass1  # Должно вызвать TypeError
    except TypeError as e:
        print(f"Ошибка при сложении разных типов: {e}")

    # Работа с категориями
    category_smartphones = Category(
        "Смартфоны",
        "Высокотехнологичные смартфоны",
        [smartphone1, smartphone2]
    )

    category_grass = Category(
        "Газонная трава",
        "Различные виды газонной травы",
        [grass1, grass2]
    )

    # Добавление продуктов в категории
    try:
        category_smartphones.add_product(smartphone3)
        print("Смартфон успешно добавлен в категорию")

        category_smartphones.add_product("Not a product")  # Должно вызвать TypeError
    except TypeError as e:
        print(f"Ошибка при добавлении не продукта: {e}")

    # Вывод информации
    print("\nКатегория смартфонов:")
    for product in category_smartphones:
        print(f"  - {product}")

    print("\nКатегория газонной травы:")
    for product in category_grass:
        print(f"  - {product}")

    print(f"\nВсего категорий: {Category.total_categories}")
    print(f"Всего продуктов: {Category.total_products}")


if __name__ == "__main__":
    main()
