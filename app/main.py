import sys
from basket import Basket
from product_store import ProductStore
from offer_store import OfferStore


class CheckoutSystem(object):

    def __init__(self):
        self._product_store = ProductStore.load_from_config_file()
        self._offer_store = OfferStore.load_from_config_file()
        self._basket = None

    def _handle_add_item_to_basket(self):
        """ adds an item in the products to basket"""
        if not self._basket:
            self._basket = Basket(self._product_store, self._offer_store)
        item = input(""" 
                    Enter Product Id:{}""".format(
            self._product_store.product_ids()))
        if not self._basket.add(item):
            print("Error: Invalid Id")

    def _handle_view_basket(self):
        """ Displays current bill, if items exists """
        self._print_receipt()

    def _handle_checkout_basket(self):
        self._print_receipt()
        self._basket = None

    def _print_receipt(self):
        if self._basket:
            response = self._basket.status()
            header = """
\n```
Item\t\tPrice
----\t\t-----
"""
            footer = "```"
            total = 0
            print(header)
            for item in response:
                total = total + item['price_after_discount']
                code = item['code']
                offer_name = item['offer_name']
                quantity = item['quantity']
                discount = item['discount']
                price = item['price']
                items_discounted = item['items_discounted']
                for i in range(items_discounted):
                    print("{}\t\t {}".format(code, price))
                    print("\t{}\t-{}".format(offer_name, discount))
                for i in range(quantity-items_discounted):
                    print("{}\t\t {}".format(code, price))
            print("--------------------------------")
            print("\t\t {}".format(round(total,2)))
            print(footer)
        else:
            print("Info: Nothing in Basket")

    def _menu(self):
        """ Main Menu For Farmers Market """

        print()

        choice = input("""
               Farmers Market Checkout System)
                      A: Add item
                      V: View Basket
                      C: Checkout
                      Q: Quit/Log Out

                      Please enter your choice: """)
        if choice == 'A' or choice == 'a':
            self._handle_add_item_to_basket()
        elif choice == 'V' or choice == 'v':
            self._handle_view_basket()
        elif choice == 'C' or choice == 'c':
            self._handle_checkout_basket()
        elif choice == 'Q' or choice == 'q':
            sys.exit(0)

    def start(self):
        while True:
            self._menu()


if __name__ == '__main__':
    system = CheckoutSystem()
    system.start()
