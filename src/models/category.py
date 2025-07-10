from typing import List, Optional
from src.models.product import Product
from src.models.category_iterator import CategoryIterator
import copy  # Добавляем импорт модуля copy

class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return copy.copy(self.__products)  # Возвращаем копию списка

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return CategoryIterator(self.__products)

    def __repr__(self):
        return f"Category(name={self.name!r}, description={self.description!r})"
