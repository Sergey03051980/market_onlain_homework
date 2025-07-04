class Product:
    def __init__(self, name, price, quantity, description=None):
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом")

        # Сохраняем параметры в атрибуты объекта
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.description = description

    def __str__(self):
        return f"Product('{self.name}', price={self.price})"  # Формат как в тесте

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
