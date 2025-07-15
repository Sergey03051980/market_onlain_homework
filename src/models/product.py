from .base_product import BaseProduct
from src.models.exceptions import ZeroQuantityError
from src.models.logging_mixin import LoggingMixin

class Product(LoggingMixin):
    def __init__(self, name, description, price, quantity):
        if quantity <= 0:
            raise ZeroQuantityError()
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()  # Инициализация миксина

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
