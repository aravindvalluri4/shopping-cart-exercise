import unittest
from product_store import Product, ProductStore, ProductNotFoundException

class ProductStoreTest(unittest.TestCase):
    """Test ProductStore """

    def setUp(self):
        products = []
        products.append(Product('CH1', 'Chai', 3.11))
        products.append(Product('AP1', 'Apples', 6.00))
        self.product_store = ProductStore(products)


    def test_product_found(self):
        self.assertEqual('CH1', self.product_store.get_product('CH1').code)
        self.assertEqual('AP1', self.product_store.get_product('AP1').code)

    def test_product_not_found(self):
        with self.assertRaises(ProductNotFoundException) :self.product_store.get_product('CH2')


class ProductTest(unittest.TestCase):
    """Test Product"""

    def setUp(self):
        self.product = Product('CH1', 'Chai', 3.11)

    def test_getters(self):
        self.assertEqual('CH1', self.product.code)
        self.assertEqual('Chai', self.product.name)
        self.assertEqual(3.11, self.product.price)

    def test_set_product_fails(self):
        try:
            self.product.price = 2.0
            self.assertTrue(False)
        except:
            self.assertTrue(True)



