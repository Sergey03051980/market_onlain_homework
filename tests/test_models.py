import pytest
from src.models.product import Product
from src.models.category import Category


def test_product_initialization():
    """Тест инициализации продукта"""
    product = Product("Test Product", 1000.0, 10, "Test Description")
    assert product.name == "Test Product"
    assert product.price == 1000.0
    assert product.quantity == 10
    assert product.description == "Test Description"


def test_product_string_representation():
    """Тест строкового представления продукта"""
    product = Product("Test Product", 1000.0, 10)
    assert str(product) == "Product('Test Product', price=1000.0)"


def test_product_negative_price():
    """Тест валидации отрицательной цены"""
    with pytest.raises(ValueError, match="Цена должна быть положительным числом"):
        Product("Invalid", -100, 5)


def test_product_zero_quantity():
    """Тест нулевого количества"""
    product = Product("Test", 100, 0)
    assert product.quantity == 0


def test_category_initialization():
    """Тест инициализации категории"""
    product = Product("Test Product", 1000.0, 10)
    category = Category("Test Category", "Test Description", [product])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert len(category.products) == 1


def test_category_count_increment():
    """Тест счетчика категорий"""
    initial_count = Category.get_total_categories()
    category = Category("New Category", "Description")
    assert Category.get_total_categories() == initial_count + 1


def test_product_count_increment():
    """Тест счетчика продуктов"""
    initial_count = Category.get_total_products()
    category = Category("New Category", "Description", [
        Product("P1", 100, 1),
        Product("P2", 200, 2)
    ])
    assert Category.get_total_products() == initial_count + 2


def test_load_from_json(json_path):
    """Тест загрузки данных из JSON"""
    from src.utils.load_data import load_categories_from_json
    categories = load_categories_from_json(json_path)
    assert len(categories) == 1
    assert len(categories[0].products) == 1


def test_json_loading_counts(json_path):
    """Тест счетчиков после загрузки из JSON"""
    from src.utils.load_data import load_categories_from_json
    initial_categories = Category.get_total_categories()
    initial_products = Category.get_total_products()

    categories = load_categories_from_json(json_path)

    assert Category.get_total_categories() == initial_categories + 1
    assert Category.get_total_products() == initial_products + 1


def test_empty_category():
    """Тест создания категории без продуктов"""
    category = Category("Empty", "Category")
    assert len(category.products) == 0
