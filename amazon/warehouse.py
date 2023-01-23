class WareHouse:
    def __init__(self):
        self.wareHouse = {}

    def add_product(self, product, count):

        if self.wareHouse.get(product.get_name(), 0):
            self.wareHouse[product.get_name()][1] += count
        else:
            self.wareHouse[product.get_name()] = [product, count]

    def get_info(self, name):
        self.wareHouse[name][0].info()

    def dell_product(self, name):
        if self.wareHouse[name][1] == 0:
            print("No this product")
            return 0

        if self.wareHouse[name][1] - 1 == 0:
            self.wareHouse[name][1] -= 1
            x = self.wareHouse[name]
            del self.wareHouse[name]
            print("Empty")
            return x
        else:
            self.wareHouse[name][1] -= 1
            return self.wareHouse[name][0]
