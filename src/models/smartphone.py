from src.models.product import Product

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __repr__(self):
        base_repr = super().__repr__()[:-1]
        return f"{base_repr}, efficiency={self.efficiency}, model={self.model!r}, memory={self.memory}, color={self.color!r})"
