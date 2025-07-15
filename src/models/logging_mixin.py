class LoggingMixin:
    def __init__(self, *args, **kwargs):
        self._logged_message = (
            f"Создан объект {self.__class__.__name__} с параметрами: "
            f"name={getattr(self, 'name', '?')}, "
            f"description={getattr(self, 'description', '?')}, "
            f"price={getattr(self, 'price', '?')}, "
            f"quantity={getattr(self, 'quantity', '?')}"
        )
        print(self._logged_message)
        super().__init__(*args, **kwargs)

