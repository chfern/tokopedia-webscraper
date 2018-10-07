from common.base.item import Item

class TokopediaItem(Item):
    @classmethod
    def extract_rp_price_number(class_, price_str):
        """
        Extract price number e.g: Rp. 90.000 to: 90000  (int)
        """
        price = price_str.lower().replace('rp', '').replace('.', '')
        price = int(price)
        return price

    @classmethod
    def extract_rating_from_brackets(class_, rating_str):
        """
        Extract rating number from brackets. e.g: (30), to 30
        """
        rating = rating_str.replace('(', '').replace(')', '')
        return int(rating)
