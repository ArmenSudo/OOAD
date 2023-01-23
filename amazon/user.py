from shopping_card import Shopping_card


class User:
    id_user = 0

    def __init__(self, name, surname, email):
        self._shopping_card = Shopping_card()
        self._name = name
        self._surname = surname
        self._email = email
        self._id = User.id_user
        User.id_user += 1

    def add_product(self, product):
        self._shopping_card.add_product(product)

    def dell_product(self, product, count):
        self._shopping_card.dell_product(product, count)

    def shopings(self):
        return self._shopping_card.get_shopings()

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def get_id(self):
        return self._id

    def get_surname(self):
        return self._surname



