import types


class Order:
    morning_discount = 0.25
    elder_discount = 0.90

    def __init__(self, price, strategy=None):
        self.price = price
        if strategy:
            self.final_price = types.MethodType(strategy, self)

    def final_price(self):
        return self.price - self.price * self.morning_discount


def morning_discount(self):
    return round(self.price - self.price * self.morning_discount)


def elder_discount(self):
    return round(self.price - self.price * self.elder_discount)
