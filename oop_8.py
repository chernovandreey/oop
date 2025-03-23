class Shopping:
    item_price = []
    item_bag = []
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_item(self):
        Shopping.item_bag.append(self.name)
        Shopping.item_price.append(self.price)

    @classmethod
    def del_item(cls, item_name):
        if item_name in cls.item_bag:
            index = cls.item_bag.index(item_name)
            cls.item_bag.pop(index)
            cls.item_price.pop(index)
            print(f"Товар {item_name} удалён из корзины")
        else:
            print(f"Товар {item_name} не найден в корзине")

    @classmethod
    def calculate_price(cls):
        return sum(cls.item_price)


item1 = Shopping("хлеб", 40)
item2 = Shopping("масло", 150)

item1.add_item()
print(Shopping.calculate_price())
item2.add_item()
print(Shopping.calculate_price())
Shopping.del_item("хлеб")
print(Shopping.calculate_price())
