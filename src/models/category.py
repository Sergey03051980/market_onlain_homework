from src.models.product import Product
import copy  # Добавляем импорт модуля copy

class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        return copy.copy(self.__products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        return iter(self.__products)

    def __repr__(self):
        return f"Category(name={self.name!r}, description={self.description!r})"
