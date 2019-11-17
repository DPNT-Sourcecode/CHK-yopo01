
prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
# Special offers ordered in a list from better to worse
special_offers = {'A': [(5,200),(3,130)], 'B':[(2,45)]} #3A for 130, 5A for 200 , 2B for 45
get_free_offers = {'E':[(2,(1,'B'))]} # 2E get one B free
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    total_price = 0
    distinct_skus = list(set(skus))
    # Check for invalid input
    for sku in distinct_skus:
        if sku not in prices.keys():
            return -1

    # Calculate the shopping cart
    cart = get_value_counts(skus)
    # Remove free items from cart
    for sku in get_free_offers.keys():
        cart_reduced = remove_free_items_from_cart(cart, sku)

    # Calculate the prices
    for sku in cart_reduced.keys():
        so_applied=False
        number_of_occurrencies = cart_reduced[sku]
        if sku in special_offers.keys():
            total_price += apply_special_offers(number_of_occurrencies, sku)
            so_applied = True
        if not so_applied:
            total_price += number_of_occurrencies * prices[sku]
    return total_price

def get_value_counts(skus):
    distinct_skus = list(set(skus))
    value_counts = {}
    for sku in distinct_skus:
        value_counts[sku] = skus.count(sku)
    return value_counts

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

def remove_free_items_from_cart(cart, sku):
    quotient, reminder = divmod(cart[sku], get_free_offers[sku][0][0])
    item_to_remove = get_free_offers[sku][0][1][1]
    if item_to_remove in cart.keys():
        cart[item_to_remove]-= quotient
        if cart[item_to_remove] < 0:
            cart[item_to_remove] = 0
    return cart


if __name__ == '__main__':
    assert(checkout('E')==40)
    assert(checkout('ABCDE')==155)
    assert(checkout('EEB')==80)
    assert(checkout('EE')==80)
    assert(checkout('EEEEBB')==160)
    assert(checkout('BEBEEE')==160)






