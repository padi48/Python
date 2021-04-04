class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.old_price = price

    def discount(self, percentage):
        self.old_price = self.price
        new_price = self.price * (1 - percentage/100)
        self.price = round(new_price)

    def __str__(self):
        print(f'{self.name}, {self.price}')


tmt = Item("tomato", 53)
tmt.discount(30)
tmt.__str__()
