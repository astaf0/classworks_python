class Order:
    def __init__(self, items, shipping):
        self.items = items
        self.shipping = shipping

    def get_shipping_cost(self):
        self.shipping.get_cost()


class AirShipping:
    def get_cost(self):