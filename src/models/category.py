from typing import List
from .product import Product  # Относительный импорт внутри пакета

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __repr__(self):
        return f"Category({self.name!r}, products={self.products})"
