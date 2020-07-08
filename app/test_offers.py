import unittest
from offers import BuyOneGetOneOffer, MinimumBuyOffer, GetDiscountOnOffer
from item import Item

from product_store import Product


class BuyOneGetOneOfferTest(unittest.TestCase):
    """Test BuyOneGetOne"""

    def setUp(self):
        self.items = []
        self.items.append(Item(Product('CF1', 'Cofee', 11.23), None,20))
        self.items.append(Item(Product('CF1', 'Cofee', 11.23), None, 21))
        self.items.append(Item(Product('Ch1', 'Chai', 3.11), None, 20))
        self.items.append(Item(Product('MK1', 'Milk', 4.75), None, 2))
        self.offers = []

    def test_similar_product_unlimited(self):
        offer = BuyOneGetOneOffer('BOGO', 'CF1', 'CF1', None)
        # even items, discount applied on 10 items
        price, items_discounted = offer.calculate(self.items[0])
        self.assertEqual(10, items_discounted)
        self.assertEqual(112.30, price)

        # odd items, 1 item has not mtch so 11 items price caliculated
        price, items_discounted = offer.calculate(self.items[1])
        self.assertEqual(10, items_discounted)
        self.assertEqual(123.53, price)

    def test_similar_product_limited(self):
        offer = BuyOneGetOneOffer('BOGO', 'CF1', 'CF1', 5)
        # limit reached
        price, items_discounted = offer.calculate(self.items[0])
        self.assertEqual(5, items_discounted)
        self.assertEqual(168.45, price)

        offer = BuyOneGetOneOffer('BOGO', 'CF1', 'CF1', 50)
        # limit not reached
        price, items_discounted = offer.calculate(self.items[0])
        self.assertEqual(10, items_discounted)
        self.assertEqual(112.30, price)

    def test_different_product_unlimited(self):
        offer = BuyOneGetOneOffer('CHMK', 'Ch1', 'MK1', None)
        price, items_discounted = offer.calculate(self.items[2], self.items[3])
        self.assertEqual(2, items_discounted)
        self.assertEqual(0, price)

    def test_different_product_limited(self):
        offer = BuyOneGetOneOffer('CHMK', 'Ch1', 'MK1', 1)
        price, items_discounted = offer.calculate(self.items[2], self.items[3])
        self.assertEqual(1, items_discounted)
        self.assertEqual(4.75, price)


class MinimumBuyOfferTest(unittest.TestCase):
    """Test MinimumBuyOffer"""

    def setUp(self):
        self.items = []
        self.items.append(Item(Product('AP1', 'Apple', 6.00), None,10))
        self.items.append(Item(Product('AP1', 'Apple', 6.00), None, 6))

    def test_min_bought(self):
        offer = MinimumBuyOffer('APPL', 'AP1', 1.5, 7)
        price, items_discounted = offer.calculate(self.items[0])
        self.assertEqual(10, items_discounted)
        self.assertEqual(45.0, price)

    def test_min_not_bought(self):
        offer = MinimumBuyOffer('APPL', 'AP1', 1.5, 7)
        price, items_discounted = offer.calculate(self.items[1])
        self.assertEqual(6, items_discounted)
        self.assertEqual(36.0, price)


class GetDiscountOnOfferTest(unittest.TestCase):
    """Test GetDiscountOnOffer"""

    def setUp(self):
        self.items = []
        self.items.append(Item(Product('OM1', 'Oats', 3.69), None, 10))
        self.items.append(Item(Product('AP1', 'Apple', 6.00), None, 6))
        self.items.append(Item(Product('AP1', 'Apple', 6.00), None, 16))

    def test_items_gt_target(self):
        offer = GetDiscountOnOffer('APOM', 'OM1', 'AP1', 3.0)
        price, items_discounted = offer.calculate(self.items[0], self.items[1])
        self.assertEqual(6, items_discounted)
        self.assertEqual(18.0, price)

    def test_items_lt_target(self):
        offer = GetDiscountOnOffer('APOM', 'OM1', 'AP1', 3.0)
        price, items_discounted = offer.calculate(self.items[0], self.items[2])
        self.assertEqual(10, items_discounted)
        self.assertEqual(66.0, price)
