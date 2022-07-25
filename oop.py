class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{gd.name}: {gd.price}" for gd in self.goods]


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Product):
    pass


class TV(Product):
    pass


class Notebook(Product):
    pass


class Cup(Product):
    pass


tv1 = TV('Sony', 19999)
tv2 = TV('LG', 234324)
table = Table('Super', 299)
cup = Cup('Appetite', 19)
cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(cup)

print(cart.get_list())
