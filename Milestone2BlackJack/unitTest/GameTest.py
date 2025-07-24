import unittest
from Milestone2BlackJack.Game import show_menu

class MyTestCase(unittest.TestCase):

    def test_show_menu(self):
        show_menu()

if __name__ == '__main__':
    unittest.main()
