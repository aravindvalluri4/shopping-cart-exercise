import json

class ProductNotFoundException(Exception):
    """Thrown if product is not found"""
    pass


class Product(object):
    """Holds information about a product in farmer's market"""

    def __init__(self, product_code, name, price):
        """initialize a product"""
        self._code = product_code
        self._name = name
        self._price = price

    @property
    def code(self):
        """product code getter"""
        return self._code

    @property
    def name(self):
        """product name getter"""
        return self._name

    @property
    def price(self):
        """product price getter"""
        return self._price

    def __repr__(self):
        return '({},{},{})'.format(self.code, self.name, self.price)


class ProductStore(object):
    """Holds the information of products """

    def __init__(self, products):
        """ initialize the product store """
        self._products = {product.code: product for product in products}

    def get_product(self, code):
        """ returns a product with given product code, else raise exception """
        if code in self._products:
            return self._products[code]
        raise ProductNotFoundException

    def product_ids(self):
        """returns list of product ids"""
        return [code for code in self._products.keys()]

    @classmethod
    def load_from_config_file(cls, file='config/products.json'):
        with open(file) as f:
            data = json.load(f)
        products = list()
        for product in data['products']:
            p = Product(product['code'], product['name'], product['price'])
            products.append(p)
        return cls(products)
