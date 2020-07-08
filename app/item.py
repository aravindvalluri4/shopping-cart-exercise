class Item(object):
    """Represents an Item in Basket"""

    def __init__(self, product, offers, quantity=0):
        self._product = product
        self._offers = offers
        self._quantity = quantity

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @property
    def offers(self):
        return self._offers

    def add(self, quantity=1):
        """ by default increase items by 1"""
        self._quantity = self._quantity + quantity

    def remove(self, quantity=1):
        """ by default increase items by 1"""
        self._quantity = self._quantity - quantity
        if self._quantity < 0:
            self._quantity = 0

    def __repr__(self):
        return "({},{}, {})".format(self.product.code, self.offers, self.quantity)
