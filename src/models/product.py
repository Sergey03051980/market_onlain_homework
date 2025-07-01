class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Цена должна быть положительной")  # Добавляем валидацию

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.name!r}, price={self.price})"
