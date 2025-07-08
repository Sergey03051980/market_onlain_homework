import pytest
from pathlib import Path
from src.models.product import Product
from src.models.category import Category

@pytest.fixture
def sample_product():
    return Product("Test Product", 1000.0, 10, "Test Description")

@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Description", [sample_product])

@pytest.fixture
def json_path(tmp_path):
    path = tmp_path / "products.json"
    data = [
        {
            "name": "Test Category",
            "description": "Test Description",
            "products": [
                {
                    "name": "Test Product",
                    "price": 1000.0,
                    "quantity": 10,
                    "description": "Test Description"
                }
            ]
        }
    ]
    import json
    path.write_text(json.dumps(data), encoding='utf-8')
    return path
