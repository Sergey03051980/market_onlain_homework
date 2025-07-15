import pytest
from src.models import BaseProduct, Product, Smartphone, LawnGrass, Category
from io import StringIO
import sys
from src.models.exceptions import ZeroQuantityError

def test_product_creation():
    """Тест создания продукта"""
    product = Product(name="Телефон", description="Смартфон", price=10000, quantity=5)
    assert product.name == "Телефон"
    assert product.price == 10000


def test_product_addition():
    """Тест сложения продуктов"""
    p1 = Product(name="Телефон", description="Смартфон", price=10000, quantity=5)
    p2 = Product(name="Ноутбук", description="Игровой", price=50000, quantity=2)
    assert p1 + p2 == 10000 * 5 + 50000 * 2


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством"""
    with pytest.raises(ZeroQuantityError):
        Product(name="Телефон", description="Смартфон", price=10000, quantity=0)


def test_category_average_price():
    """Тест подсчёта средней цены"""
    category = Category(name="Электроника", description="Техника")

    # Пустая категория
    assert category.average_price() == 0

    # Добавляем товары
    p1 = Product(name="Телефон", description="Смартфон", price=10000, quantity=5)
    p2 = Product(name="Ноутбук", description="Игровой", price=50000, quantity=2)
    category.add_product(p1)
    category.add_product(p2)

    assert category.average_price() == 30000  # (10000 + 50000) / 2


def test_logging_mixin():
    """Проверка работы миксина логирования"""
    p = Product(name="Test", description="Desc", price=100, quantity=5)
    assert hasattr(p, '_logged_message')
    assert "Test" in p._logged_message


def test_logging_mixin_output(capsys):
    """Проверка вывода в консоль"""
    _ = Product(name="Test", description="Desc", price=100, quantity=5)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
