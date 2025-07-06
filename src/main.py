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

    # 4. Тестирование приватной цены
    print("\n=== ТЕСТИРОВАНИЕ ПРИВАТНОЙ ЦЕНЫ ===")
    test_private_price()


def manual_demo():
    """Демонстрация ручного создания объектов"""
    # Сброс счетчиков
    Category.reset_counters()

    # Создание товаров с использованием именованных параметров
    products = [
        Product(name="Xiaomi", price=25000.0, quantity=10, description="Смартфон"),
        Product(name="Samsung", price=45000.0, quantity=5, description="Планшет")
    ]

    # Создание категории
    category = Category(name="Электроника", description="Техника", products=products)

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

    # Добавляем новый продукт
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


def test_private_price():
    """Тестирование работы с приватной ценой"""
    print("\nТестирование приватной цены продукта:")

    # Создаем тестовый продукт
    test_product = Product(name="Тестовый", price=1000, quantity=1)
    print(f"Создан продукт: {test_product}")

    # 1. Проверяем геттер
    print(f"Текущая цена: {test_product.price} руб.")

    # 2. Проверяем сеттер
    test_product.price = 1500
    print(f"Новая цена: {test_product.price} руб.")

    # 3. Пробуем установить недопустимые значения
    try:
        test_product.price = -100
    except ValueError as e:
        print(f"Ошибка при установке отрицательной цены: {e}")

    try:
        test_product.price = "тысяча"
    except TypeError as e:
        print(f"Ошибка при установке строки вместо числа: {e}")

    # 4. Пробуем обратиться к приватному атрибуту
    try:
        print(test_product.__price)
    except AttributeError as e:
        print(f"Попытка доступа к приватному атрибуту __price: {e}")


if __name__ == "__main__":
    main()
