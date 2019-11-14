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

if __name__ == '__main__':
    print(hello('Tom'))
    class TestHello(unittest.TestCase):
        def test_hello(self):
            self.assertEqual((hello('Tom'),"Hello, World!")
    




