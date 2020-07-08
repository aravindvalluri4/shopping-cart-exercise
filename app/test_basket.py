import unittest

from basket import Basket
from offer_store import OfferStore
from product_store import ProductStore


class BasketTest(unittest.TestCase):


    def setUp(self):
         
        ps = ProductStore.load_from_config_file()
        os = OfferStore.load_from_config_file()
        self.basket = Basket(ps, os)


    def _get_total_price(self, response):
        total_price =0 
        for item in response:
              total_price = total_price + item['price_after_discount'] 
        return total_price


    def test_empty_basket_view(self):
      self.assertEqual([], self.basket.status()) 

    def test_no_offers(self):
      self.basket.add('AP1')
      self.basket.add('CH1')
      response = self.basket.status()
      price = self._get_total_price(response)
      self.assertEqual(price, 9.11) 


    def test_multi_offers(self):
      
      self.basket.add('AP1')
      self.basket.add('AP1')
      self.basket.add('AP1')
      self.basket.add('CH1')
      self.basket.add('MK1')
      response = self.basket.status()
      price = self._get_total_price(response)
      self.assertEqual(price, 16.61) 

   

