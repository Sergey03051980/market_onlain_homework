class Product:
    def __init__(self, name, price, quantity, description=None):
        self.name = name
        self.__price = 0  # Приватный атрибут
        self.quantity = quantity
        self.description = description
        self.price = price  # Используем сеттер для инициализации

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с валидацией"""
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом")
        if value <= 0:
            raise ValueError("Цена должна быть положительным числом")
        self.__price = float(value)

    def __str__(self):
        """Для соответствия тестам"""
        return f"Product('{self.name}', price={self.price})"

    def __repr__(self):
        """Для отладки и разработки"""
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"

    def display_info(self):
        """Пользовательское отображение информации о продукте"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"
