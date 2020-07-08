class IOffer(object):

    def __init__(self, name, product, target_product, discount):
        self.name = name
        self.product = product
        self.target_product = target_product
        self.discount = discount

    def calculate(self, item, target_item=None):
        pass


# TODO can be extend it BuyXGetX
class BuyOneGetOneOffer(IOffer):

    def __init__(self, name, product, target_product, limit):
        super().__init__(name, product, target_product, 0)
        self.limit = limit

    def _calculate_for_same_item(self, item):
        total_price = 0
        items_discounted = item.quantity // 2
        if self.limit and items_discounted > self.limit:
            items_discounted = self.limit
        total_price = (item.quantity - items_discounted) * item.product.price
        return round(total_price, 2), items_discounted

    def _calculate_for_different_items(self, item, target_item):
        items_discounted = item.quantity
        if self.limit and items_discounted > self.limit:
            items_discounted = self.limit
        items_not_discounted = target_item.quantity - items_discounted
        if items_not_discounted <= 0:
            return 0, target_item.quantity
        else:
            total_price = items_not_discounted * target_item.product.price
            return round(total_price, 2), items_discounted

    def calculate(self, item, target_item=None):
        if self.product == self.target_product:
            self.discount = item.product.price
            return self._calculate_for_same_item(item)
        else:
            self.discount = target_item.product.price
            return self._calculate_for_different_items(item, target_item)


# TODO extend to a different target product
class MinimumBuyOffer(IOffer):
    """Handles cass where discount is applied if min amount products bought"""

    def __init__(self, name, product, discount, minimum_buy):
        super().__init__(name, product, target_product=product, discount=discount)
        self.minimum_buy = minimum_buy

    def calculate(self, item, target_item=None):
        discount = 0
        if item.quantity >= self.minimum_buy:
            discount = self.discount
        total_price = (item.product.price - discount) * item.quantity
        return round(total_price, 2), item.quantity


class GetDiscountOnOffer(IOffer):
    """Handles Discount on target product"""

    def __init__(self, name, product, target_product, discount):
        super().__init__(name, product, target_product, discount)

    def calculate(self, item, target_item=None):
        items_eligible_for_discount = target_item.quantity
        if items_eligible_for_discount > item.quantity:
            # only items quantity is eligible for discount
            items_eligible_for_discount = item.quantity
        discount_price = (target_item.product.price - self.discount) * items_eligible_for_discount
        not_discounted_price = target_item.product.price * \
                               (target_item.quantity - items_eligible_for_discount)
        total_price = discount_price + not_discounted_price
        return round(total_price, 2), items_eligible_for_discount


class OfferFactory(object):
    """creates offers"""

    @staticmethod
    def create(offer):
        if offer["type"] == 'BuyOneGetOneOffer':
            return BuyOneGetOneOffer(offer["name"], offer["product"],
                                     offer["target_product"], offer["offer_limit"])
        elif offer["type"] == 'MinimumBuyOffer':
            return MinimumBuyOffer(offer["name"], offer["product"],
                                   offer["discount"], offer["minimum_items_to_buy"])
        elif offer["type"] == 'GetDiscountOnOffer':
            return GetDiscountOnOffer(offer["name"], offer["product"], offer["target_product"],
                                      offer["discount"])
        else:
            return None
