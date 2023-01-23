class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def info(self):
        print(self.name, self.price, self.description)