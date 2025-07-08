from typing import List, Optional
from src.models.product import Product


class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []  # Публичный атрибут

        Category.total_categories += 1
        Category.total_products += len(self.products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")
        self.products.append(product)
        Category.total_products += 1

    @classmethod
    def get_total_categories(cls):
        return cls.total_categories

    @classmethod
    def get_total_products(cls):
        return cls.total_products

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)}"

    def __repr__(self):
        return f"Category(name={self.name!r}, description={self.description!r})"

    @classmethod
    def reset_counters(cls):
        """Сбрасывает счетчики категорий и продуктов"""
        cls.total_categories = 0
        cls.total_products = 0