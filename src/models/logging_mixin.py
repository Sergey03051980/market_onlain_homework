class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Сначала инициализируем родительские классы
        self._logged_message = (
            f"Создан объект {self.__class__.__name__} с параметрами: "
            f"name={self.name}, description={self.description}, "
            f"price={self.price}, quantity={self.quantity}"
        )
        print(self._logged_message)
