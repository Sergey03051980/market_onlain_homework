import copy  # Добавляем импорт модуля copy
from .exceptions import ZeroQuantityError

class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def average_price(self):
        try:
            total = sum(product.price for product in self.products)
            return total / len(self.products)
        except ZeroDivisionError:
            return 0
