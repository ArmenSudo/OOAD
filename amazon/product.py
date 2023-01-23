class Product:
    def __init__(self, name, price, description):
        self._name = name
        self._price = price
        self._description = description

    def info(self):
        print(self._name, self._price, self._description)

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_description(self):
        return self._description

    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_description(self, description):
        self._description = description
