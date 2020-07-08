import json

from item import Item
from product_store import ProductStore, Product, ProductNotFoundException
from offer_store import OfferStore


class Basket(object):
    """basket holds different products"""

    def __init__(self, product_store, offer_store):
        """ init """
        # dict of product.code: item
        self._items = {}
        self._product_store = product_store
        self._offer_store = offer_store

    def add(self, product_code, quantity=1):
        """ add an item to basket """
        try:
            product = self._product_store.get_product(product_code)
            if product.code in self._items:
                # increase quanity by 1
                self._items[product.code].add(quantity)
            else:
                offers = self._offer_store.get_offers_on_product(product.code)
                new_item_in_basket = Item(product, offers, quantity=1)
                self._items[product.code] = new_item_in_basket
        except ProductNotFoundException:
            return False
        else:
            return True

    def remove(self, product_code, quantity=1):
        """ removes an item from basket """
        if product_code in self._items:
            self._items[product_code].remove(quantity)
            return True
        return False

    def _apply_best_offer(self, item, total_price):
        best_price = total_price
        items_discounted = 0
        discount = 0
        offer_name = None
        if not item.offers:
            return best_price, items_discounted, discount, offer_name
        for offer in item.offers:
            if offer.product in self._items:
                price, count = offer.calculate(self._items[offer.product], item)
                if price < best_price:
                    best_price, items_discounted = price, count
                    discount = offer.discount
                    offer_name = offer.name
        return best_price, items_discounted, discount, offer_name

    def _items_after_discount(self):
        response = []
        for item in self._items.values():
            actual_total_price = item.product.price * item.quantity
            price_after_discount, items_discounted, discount, name = self._apply_best_offer(item, actual_total_price)
            response_item = dict(code=item.product.code,
                                 price=item.product.price,
                                 quantity=item.quantity,
                                 actual_total_price=actual_total_price,
                                 items_discounted=items_discounted,
                                 price_after_discount=price_after_discount,
                                 discount= discount,
                                 offer_name= name)
            response.append(response_item)
        return response

    def status(self):
        """ returns """
        return self._items_after_discount()

    def checkout(self):
        """ checkout """
        pass
