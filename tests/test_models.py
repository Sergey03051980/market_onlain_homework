import pytest
from src.models.product import Product
from src.models.category import Category
from src.models.category_iterator import CategoryIterator


def test_product_str():
    """Тест строкового представления продукта"""
    product = Product("Телефон", 10000, 5)
    assert str(product) == "Телефон, 10000 руб. Остаток: 5 шт."


def test_product_repr():
    """Тест repr представления продукта"""
    product = Product("Телефон", 10000, 5, "Смартфон")
    assert repr(product) == "Product(name='Телефон', price=10000, quantity=5)"


def test_product_price_setter():
    """Тест сеттера цены"""
    product = Product("Телефон", 10000, 5)

    # Проверка валидного значения
    product.price = 15000
    assert product.price == 15000

    # Проверка невалидных значений
    with pytest.raises(ValueError):
        product.price = -100

    with pytest.raises(TypeError):
        product.price = "десять тысяч"


def test_product_addition():
    """Тест сложения продуктов"""
    p1 = Product("Телефон", 10000, 5)
    p2 = Product("Ноутбук", 50000, 2)

    # Проверка сложения
    assert p1 + p2 == 10000 * 5 + 50000 * 2

    # Проверка сложения с неправильным типом
    with pytest.raises(TypeError):
        p1 + "не продукт"


def test_category_str():
    """Тест строкового представления категории"""
    products = [
        Product("Телефон", 10000, 5),
        Product("Ноутбук", 50000, 2)
    ]
    category = Category("Электроника", "Техника", products)
    assert str(category) == "Электроника, количество продуктов: 7 шт."


def test_category_repr():
    """Тест repr представления категории"""
    category = Category("Электроника", "Техника")
    assert repr(category) == "Category(name='Электроника', description='Техника')"


def test_category_iteration():
    """Тест итерации по категории"""
    products = [
        Product("Телефон", 10000, 5),
        Product("Ноутбук", 50000, 2)
    ]
    category = Category("Электроника", "Техника", products)

    # Проверка итерации
    product_names = [p.name for p in category]
    assert product_names == ["Телефон", "Ноутбук"]

    # Проверка пустой категории
    empty_category = Category("Пустая", "Категория")
    assert list(empty_category) == []


def test_category_add_product():
    """Тест добавления продукта в категорию"""
    category = Category("Электроника", "Техника")
    product = Product("Телефон", 10000, 5)

    # Проверка добавления
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0].name == "Телефон"


def test_category_products_property():
    """Тест свойства products"""
    products = [
        Product("Телефон", 10000, 5),
        Product("Ноутбук", 50000, 2)
    ]
    category = Category("Электроника", "Техника", products)

    # Проверка что возвращается эквивалентный список
    assert category.products == products

    # Проверка что это другой объект (копия)
    assert category.products is not products

    # Проверка что изменения копии не влияют на оригинал
    products_copy = category.products
    products_copy.append(Product("Планшет", 30000, 3))
    assert len(category.products) == 2  # Оригинал не изменился


def test_product_with_description():
    """Тест продукта с описанием"""
    product = Product("Телефон", 10000, 5, "Смартфон")
    assert product.description == "Смартфон"
