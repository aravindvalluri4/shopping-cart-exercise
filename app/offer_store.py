import json
from offers import OfferFactory


class OfferStore(object):
    """parses and stores offers data"""

    def __init__(self, offers):
        # get list of offers on target product
        self._offers = dict()
        for offer in offers:
            code = offer['target_product']
            if code not in self._offers:
                self._offers[code] = [OfferFactory.create(offer)]
            else:
                self._offers[code].append(OfferFactory.create(offer))

    def get_offers_on_product(self, code):
        """Returns list of offers available on product"""
        if code in self._offers:
            return self._offers[code]
        else:
            return None

    @classmethod
    def load_from_config_file(cls, file='config/offers.json'):
        with open(file) as f:
            data = json.load(f)
        return cls(data['offers'])
