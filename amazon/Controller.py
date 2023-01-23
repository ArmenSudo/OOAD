from warehouse import WareHouse
from user import User
from product import Product

ware_house_all = WareHouse()


def add_in_wareHouser(product, count):
    ware_house_all.add_product(product, count)
    ware_house_all.get_info(product.name)


iphone = Product('Iphone', 150, 'Lavna')
samsung = Product('Samsung', 150, 'Lavna')
xiaomi = Product('Xiaomi', 150, 'Lavna')

add_in_wareHouser(iphone, 15)
add_in_wareHouser(samsung, 10)
add_in_wareHouser(xiaomi, 5)


def make_user(name, surname, email):
    return User(name, surname, email)


armen = make_user('Armen', 'Harutyunyan', 'harmen2024@gmail.com')
anna = make_user('Anna', 'Harutyunyan', 'annnaAnna@gmail.com')

print(armen.get_id())
print(anna.get_id())


def add_product(user_name, product):
    user_name.add_product(product)


def dell_product(user_name, product):
    user_name.dell_product(product, 1)


add_product(armen, iphone)
add_product(anna, samsung)

dell_product(armen, iphone)
dell_product(armen, iphone)

dell_product(armen, iphone)
print(armen.shopings())
print(anna.shopings())