from typing import Optional, List, Iterator
from src.models.product import Product


class Category:
    _total_categories = 0
    _total_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category._total_categories += 1
        Category._total_products += len(products)

    @classmethod
    def category_count(cls):
        return cls._total_categories

    @classmethod
    def product_count(cls):
        return cls._total_products

    # Или используйте property для более удобного доступа:
    @property
    def category_count_property(self):
        return self._total_categories

    @property
    def product_count_property(self):
        return self._total_products
