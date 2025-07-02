import pytest
from src.models.product import Product
from src.models.category import Category
from src.utils.load_data import load_categories_from_json

def test_product_initialization(sample_product):
    """Тест инициализации продукта"""
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 1000.0
    assert sample_product.quantity == 10

def test_product_string_representation(sample_product):
    """Тест строкового представления продукта"""
    assert str(sample_product) == "Product('Test Product', price=1000.0)"

def test_product_negative_price():
    """Тест валидации отрицательной цены"""
    with pytest.raises(ValueError, match="Цена должна быть положительной"):
        Product("Invalid", "Product", -100, 5)

def test_product_zero_quantity():
    """Тест нулевого количества"""
    product = Product("Test", "Product", 100, 0)
    assert product.quantity == 0

def test_category_initialization(sample_category, sample_product):
    """Тест инициализации категории"""
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert len(sample_category.products) == 1
    assert sample_category.products[0] == sample_product


def test_category_count_increment():
    """Тест счетчика категорий"""
    assert Category.category_count() == 0  # Теперь вызываем как метод

    products = [
        Product("Product 1", "Desc 1", 100, 5),
        Product("Product 2", "Desc 2", 200, 3)
    ]
    Category("New Category", "Description", products)

    assert Category.category_count() == 1  # Вызываем как метод


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасывает счетчики перед каждым тестом"""
    Category._total_categories = 0
    Category._total_products = 0
    yield
    # Дополнительный сброс после теста (опционально)
    Category._total_categories = 0
    Category._total_products = 0


def test_product_count_increment():
    """Тест счетчика продуктов"""
    assert Category.product_count() == 0

    new_product = Product("New Product", "Desc", 500, 3)
    Category("New Category", "Description", [new_product])

    assert Category.product_count() == 1


def test_load_from_json(json_path):
    """Тест загрузки данных из JSON"""
    categories = load_categories_from_json(json_path)

    assert len(categories) >= 1
    for category in categories:
        assert isinstance(category, Category)
        assert len(category.products) >= 1
        for product in category.products:
            assert isinstance(product, Product)

def test_json_loading_counts(json_path):
    """Тест счетчиков после загрузки из JSON"""
    initial_categories = Category.category_count()
    initial_products = Category.product_count()

    categories = load_categories_from_json(json_path)
    total_products = sum(len(c.products) for c in categories)

    assert Category.category_count() == initial_categories + len(categories)
    assert Category.product_count() == initial_products + total_products


def test_empty_category():
    """Тест создания категории без продуктов"""
    category = Category("Empty", "Category", [])
    assert len(category.products) == 0
    assert Category.category_count() > 0
    assert Category.product_count() >= 0
