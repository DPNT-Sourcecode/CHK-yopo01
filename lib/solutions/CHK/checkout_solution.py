
prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
# Special offers ordered in a list from better to worse
special_offers = {'A': [(5,200),(3,130)], 'B':[(2,45)]} #3A for 130, 5A for 200 , 2B for 45
get_free_offers = {'E':[(2,(1,'B'))]} # 2E get one B free
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_price = 0
    distinct_skus = list(set(skus))
    for sku in distinct_skus:
        if sku not in prices.keys():
            return -1
        so_applied=False
        number_of_occurrencies = skus.count(sku)
        if sku in special_offers.keys():
            total_price += apply_special_offers(number_of_occurrencies, sku)
            so_applied = True
        if sku in get_free_offers.keys():
            total_price -= apply_get_free_offers(number_of_occurrencies, sku)
        if not so_applied:
            total_price += number_of_occurrencies * prices[sku]
    return total_price


def apply_special_offers(value, sku):
    """
    Applies all special offers. They need to be sorted in descending order of value for the customer
    :param value: the number of items
    :param sku: the item label
    :return: the total price for that item with the orders applied
    """
    reminder = value
    price = 0
    for special_offer in special_offers[sku]:
        quotient, reminder = divmod(reminder, special_offer[0])
        price += quotient*special_offer[1]
    return price + reminder*prices[sku]

def apply_get_free_offers( value, sku):
    quotient, reminder = divmod(value, get_free_offers[sku][0][0])

    return quotient*prices[get_free_offers[sku][0][1][1]]

if __name__ == '__main__':
    assert(checkout('E')==40)
    assert(checkout('ABCDE')==155)
    assert(checkout('EEB')==80)
    print(checkout('EE'))
    assert(checkout('EE')==80)
    assert(checkout('EEEEBB')==160)
    assert(checkout('BEBEEE')==160)





