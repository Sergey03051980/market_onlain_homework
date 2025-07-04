from utils.load_data import load_categories_from_json
from src.models.product import Product
from src.models.category import Category
from pathlib import Path


def main():
    # 1. Ручное создание объектов
    print("=== РУЧНОЕ СОЗДАНИЕ ОБЪЕКТОВ ===")
    manual_demo()

    # 2. Загрузка из JSON
    print("\n=== ЗАГРУЗКА ИЗ JSON ===")
    json_path = Path(__file__).parent.parent / "data" / "products.json"
    json_demo(json_path)

    # 3. Дополнительные тесты
    print("\n=== ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ ===")
    additional_tests()


def manual_demo():
    """Демонстрация ручного создания объектов"""
    # Сброс счетчиков
    Category.reset_counters()

    # Создание товаров
    products = [
        Product("Xiaomi", 25000.0, 10, "Смартфон"),
        Product("Samsung", 45000.0, 5, "Планшет")
    ]

    # Создание категории
    category = Category("Электроника", "Техника", products)

    # Вывод информации
    print(f"Создана категория: {category}")
    print(f"Товары: {category.products}")
    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего товаров: {Category.total_products}")


def json_demo(json_path: Path):
    """Демонстрация загрузки из JSON"""
    # Сброс счетчиков
    Category.reset_counters()

    # Загрузка данных
    categories = load_categories_from_json(json_path)

    # Вывод информации
    for category in categories:
        print(f"\nКатегория: {category.name}")
        print(f"Описание: {category.description}")
        print(f"Товары ({len(category.products)}):")
        for product in category.products:
            print(f"  - {product.name}: {product.price} руб. ({product.quantity} шт.)")

    print(f"\nВсего категорий: {Category.total_categories}")
    print(f"Всего товаров: {Category.total_products}")


def additional_tests():
    """Дополнительные тесты работы с продуктами и категориями"""
    # Сброс счетчиков
    Category.reset_counters()

    # Создаем продукты с именованными параметрами
    product1 = Product(
        name="Samsung Galaxy S23 Ultra",
        price=180000.0,
        quantity=5,
        description="256GB, Серый цвет, 200MP камера"
    )
    product2 = Product(
        name="Iphone 15",
        price=210000.0,
        quantity=8,
        description="512GB, Gray space"
    )
    product3 = Product(
        name="Xiaomi Redmi Note 11",
        price=31000.0,
        quantity=14,
        description="1024GB, Синий"
    )

    # Создаем категорию
    category1 = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    # Добавляем продукты
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    # Выводим список товаров
    print("Товары в категории:")
    print(category1.products)
    print(f"Всего продуктов: {Category.total_products}")

    # Добавляем новый продукт (с исправленным вызовом)
    product4 = Product(
        name="55\" QLED 4K",
        price=123000.0,
        quantity=7,
        description="Фоновая подсветка"
    )
    category1.add_product(product4)
    print("\nПосле добавления нового товара:")
    print(category1.products)
    print(f"Всего продуктов: {Category.total_products}")

    # Добавляем продукты через метод add_product()
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)

    # Выводим список товаров через геттер
    print("Товары в категории:")
    print(category1.products)
    print(f"Всего продуктов: {Category.total_products}")

    # Добавляем новый продукт
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print("\nПосле добавления нового товара:")
    print(category1.products)
    print(f"Всего продуктов: {Category.total_products}")

    # Тестируем класс-метод new_product
    print("\nТестирование класс-метода new_product:")
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra",
         "description": "256GB, Серый цвет, 200MP камера",
         "price": 180000.0,
         "quantity": 5}
    )
    print(f"Название: {new_product.name}")
    print(f"Описание: {new_product.description}")
    print(f"Цена: {new_product.price} руб.")
    print(f"Количество: {new_product.quantity} шт.")

    # Тестируем изменение цены
    print("\nТестирование изменения цены:")
    print(f"Текущая цена: {new_product.price} руб.")

    print("\nПопытка установить цену 800 руб.:")
    new_product.price = 800  # Должно запросить подтверждение (если реализовано доп. задание)
    print(f"Новая цена: {new_product.price} руб.")

    print("\nПопытка установить отрицательную цену (-100 руб.):")
    new_product.price = -100  # Должно вывести сообщение об ошибке
    print(f"Цена осталась: {new_product.price} руб.")

    print("\nПопытка установить нулевую цену:")
    new_product.price = 0  # Должно вывести сообщение об ошибке
    print(f"Цена осталась: {new_product.price} руб.")


if __name__ == "__main__":
    main()
