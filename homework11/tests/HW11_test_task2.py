from homework11.task2.discounts import Order, morning_discount, elder_discount


class TestDiscounts:
    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)

    def test_order_with_morning_disc(self):
        assert self.order_1.final_price() == 75

    def test_order_with_elder_disc(self):
        assert self.order_2.final_price() == 10
