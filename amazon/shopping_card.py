from collections import defaultdict
from collections import namedtuple

product_tuple = namedtuple('prod_tuple', ('product', 'count'))


class Shopping_card:
    def __init__(self):
        # self._products = {}
        self._products = defaultdict(list)

    def add_product(self, product):
        self._products[product.name].append(product)

    def get_shopings(self):
        return self._products

    def dell_product(self, product, count):
        for x in range(count):
            try:
                self._products[product.name].pop()
                if len(self._products[product.name]) == 0:
                    del self._products[product.name]
            except:
                del self._products[product.name]
                print("No Product in shopping card!")
