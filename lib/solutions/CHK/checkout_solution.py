
prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
special_offers = {'A': [(3,130),(5,200)], 'B':[(2,45)]}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    total_price = 0
    distinct_skus = list(set(skus))
    for sku in distinct_skus:
        if sku not in prices.keys():
            return -1
        number_of_occurrencies = skus.count(sku)
        if sku in special_offers.keys():
            number_of_so = number_of_occurrencies // special_offers[sku][0][0]
            number_of_single_items = number_of_occurrencies % special_offers[sku][0][0]
            total_price += number_of_single_items*prices[sku] + number_of_so*special_offers[sku][0][1]
        else:
            total_price += number_of_occurrencies * prices[sku]
    return total_price

if __name__ == '__main__':
    print(checkout('TAAACT'))




