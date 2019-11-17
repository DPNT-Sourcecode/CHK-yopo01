
prices = {'A':50, 'B':30, 'C':20, 'D':15}
special_offers = {'A': (3,130), 'B':(2,45)}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus_list = list(skus)
    for sku in skus_list:
        print(sku)

if __name__ == '__main__':
    checkout('ABC')

