import pytest
from src.models import BaseProduct, Product, Smartphone, LawnGrass, Category
from io import StringIO
import sys

def test_product_creation():
    """Тест создания базового продукта"""
    product = Product(name="Телефон", description="Смартфон", price=10000, quantity=5)
    assert product.name == "Телефон"
    assert product.price == 10000
    assert product.quantity == 5


def test_product_addition():
    """Тест сложения продуктов"""
    p1 = Product(name="Телефон", description="Смартфон", price=10000, quantity=5)
    p2 = Product(name="Ноутбук", description="Игровой", price=50000, quantity=2)

    # Проверяем сложение
    assert p1 + p2 == 10000 * 5 + 50000 * 2  # 50 000 + 100 000 = 150 000

    # Проверяем порядок сложения
    assert p2 + p1 == p1 + p2

    # Проверяем исключение при сложении с не-Product
    with pytest.raises(TypeError):
        p1 + 100


def test_base_product_abstract():
    """Проверка, что BaseProduct действительно абстрактный"""
    with pytest.raises(TypeError):
        # Попытка создать экземпляр абстрактного класса
        BaseProduct(name="Test", description="Desc", price=100, quantity=5)


def test_logging_mixin():
    """Проверка работы миксина логирования"""
    # Создаем продукт
    p = Product(name="Test", description="Desc", price=100, quantity=5)

    # Проверяем сохраненное сообщение
    assert hasattr(p, '_logged_message')
    assert "Создан объект Product с параметрами:" in p._logged_message
    assert "name=Test" in p._logged_message
    assert "description=Desc" in p._logged_message
    assert "price=100" in p._logged_message
    assert "quantity=5" in p._logged_message


def test_logging_mixin_output(capsys):
    """Проверка вывода в консоль"""
    _ = Product(name="Test", description="Desc", price=100, quantity=5)
    captured = capsys.readouterr()
    assert "Создан объект Product с параметрами:" in captured.out
