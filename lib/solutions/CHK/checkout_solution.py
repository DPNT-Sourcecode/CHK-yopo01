
prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
# Special offers ordered in a list from better to worse
special_offers = {'A': [(5,200),(3,130)], 'B':[(2,45)]} #3A for 130, 5A for 200 , 2B for 45
get_free_offers = {'E':(2,(1,'B'))} # 2E get one B free
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
            total_price = apply_special_offers(number_of_occurrencies,  special_offers[sku], sku)
        else:
            total_price += number_of_occurrencies * prices[sku]
    return total_price


def apply_special_offers(value, special_offers, sku):
    reminder = value
    price = 0
    for special_offer in special_offers:
        quotient, reminder = divmod(reminder, special_offer[0])
        print(quotient, reminder)
        price += quotient*special_offer[1]
    return price + reminder*prices[sku]

if __name__ == '__main__':
    print(checkout('AAAA'))
