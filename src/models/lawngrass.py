from src.models.product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __repr__(self):
        base_repr = super().__repr__()[:-1]
        return f"{base_repr}, country={self.country!r}, germination_period={self.germination_period!r}, color={self.color!r})"
