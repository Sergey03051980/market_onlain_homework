import pytest
from src.models.product import Product
from src.models.smartphone import Smartphone
from src.models.lawngrass import LawnGrass
from src.models.category import Category


def test_product_creation():
    """Тест создания базового продукта"""
    product = Product("Телефон", "Смартфон", 10000, 5)
    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 10000
    assert product.quantity == 5


def test_smartphone_creation():
    """Тест создания смартфона"""
    smartphone = Smartphone(
        "Galaxy S23", "Флагман", 100000, 10,
        95.5, "S23", 256, "Черный"
    )
    assert smartphone.name == "Galaxy S23"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23"
    assert smartphone.memory == 256
    assert smartphone.color == "Черный"


def test_lawngrass_creation():
    """Тест создания газонной травы"""
    grass = LawnGrass(
        "Трава", "Элитная", 500, 20,
        "Россия", "14 дней", "Зеленая"
    )
    assert grass.name == "Трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "14 дней"
    assert grass.color == "Зеленая"


def test_product_addition_same_type():
    """Тест сложения продуктов одного типа"""
    p1 = Product("Телефон", "Смартфон", 10000, 5)
    p2 = Product("Ноутбук", "Игровой", 50000, 2)
    assert p1 + p2 == 10000 * 5 + 50000 * 2


def test_smartphone_addition():
    """Тест сложения смартфонов"""
    s1 = Smartphone("S1", "Флагман", 100000, 3, 95, "S1", 256, "Черный")
    s2 = Smartphone("S2", "Бюджет", 50000, 5, 85, "S2", 128, "Синий")
    assert s1 + s2 == 100000 * 3 + 50000 * 5


def test_lawngrass_addition():
    """Тест сложения газонной травы"""
    g1 = LawnGrass("G1", "Элитная", 500, 10, "Россия", "14 дней", "Зеленая")
    g2 = LawnGrass("G2", "Обычная", 300, 20, "Беларусь", "10 дней", "Темная")
    assert g1 + g2 == 500 * 10 + 300 * 20


def test_product_addition_different_types():
    """Тест сложения продуктов разных типов"""
    p = Product("Телефон", "Смартфон", 10000, 5)
    s = Smartphone("S1", "Флагман", 100000, 3, 95, "S1", 256, "Черный")
    g = LawnGrass("G1", "Элитная", 500, 10, "Россия", "14 дней", "Зеленая")

    with pytest.raises(TypeError):
        p + s

    with pytest.raises(TypeError):
        s + g

    with pytest.raises(TypeError):
        p + g


def test_category_add_valid_product():
    """Тест добавления валидного продукта в категорию"""
    category = Category("Техника", "Электроника")
    p = Product("Телефон", "Смартфон", 10000, 5)
    s = Smartphone("S1", "Флагман", 100000, 3, 95, "S1", 256, "Черный")

    category.add_product(p)
    category.add_product(s)

    assert len(category.products) == 2


def test_category_add_invalid_product():
    """Тест добавления невалидного продукта в категорию"""
    category = Category("Техника", "Электроника")

    with pytest.raises(TypeError):
        category.add_product("Не продукт")

    with pytest.raises(TypeError):
        category.add_product(123)

    with pytest.raises(TypeError):
        category.add_product({"name": "Телефон"})


def test_product_str_representation():
    """Тест строкового представления продукта"""
    p = Product("Телефон", "Смартфон", 10000, 5)
    assert str(p) == "Телефон, 10000 руб. Остаток: 5 шт."


def test_smartphone_str_representation():
    """Тест строкового представления смартфона"""
    s = Smartphone("S1", "Флагман", 100000, 3, 95, "S1", 256, "Черный")
    assert str(s) == "S1, 100000 руб. Остаток: 3 шт."


def test_lawngrass_str_representation():
    """Тест строкового представления газонной травы"""
    g = LawnGrass("G1", "Элитная", 500, 10, "Россия", "14 дней", "Зеленая")
    assert str(g) == "G1, 500 руб. Остаток: 10 шт."


def test_category_str_representation():
    """Тест строкового представления категории"""
    p1 = Product("Телефон", "Смартфон", 10000, 5)
    p2 = Product("Ноутбук", "Игровой", 50000, 2)
    category = Category("Техника", "Электроника", [p1, p2])

    assert str(category) == "Техника, количество продуктов: 7 шт."


def test_category_total_counters():
    """Тест счетчиков категорий и продуктов"""
    Category.total_categories = 0
    Category.total_products = 0

    p1 = Product("Телефон", "Смартфон", 10000, 5)
    p2 = Product("Ноутбук", "Игровой", 50000, 2)
    category1 = Category("Техника", "Электроника", [p1, p2])
    category2 = Category("Сад", "Для дачи", [])

    assert Category.total_categories == 2
    assert Category.total_products == 2
