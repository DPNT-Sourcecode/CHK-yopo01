import unittest

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    """
    Says hello world
    param[0] = a String. Ignore for now.
    @return = a String containing a message
    """
    return "Hello, World!"

class TestCard(unittest.TestCase):
    def test_card_initial_balance(self):
        card = Card()
        self.assertEqual(card.get_balance(), 0.0)

if __name__ == '__main__':
    print(hello('Tom'))
    



