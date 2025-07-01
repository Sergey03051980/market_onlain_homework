import pytest
from pathlib import Path
from src.models.product import Product
from src.models.category import Category

@pytest.fixture
def sample_product():
    """Фикстура для тестового продукта"""
    return Product("Test Product", "Test Description", 1000.0, 10)

@pytest.fixture
def sample_category(sample_product):
    """Фикстура для тестовой категории"""
    return Category("Test Category", "Test Description", [sample_product])

@pytest.fixture
def json_path():
    """Фикстура с путем к тестовому JSON-файлу"""
    path = Path(__file__).parent.parent / "data" / "products.json"
    if not path.exists():
        pytest.skip(f"Тестовый JSON файл не найден: {path}")
    return path
