import unittest
from Milestone2BlackJack.Deck import Deck
from Milestone2BlackJack.Card import Card


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.my_deck = Deck()

    def test_create_deck_full_size(self):
        expected_size = 52
        result = self.my_deck.create_deck_cards()
        self.assertEqual(expected_size, len(result))

    def test_create_deck_contents(self):
        item = Card(Card.DIAMONDS, Card.EIGHT, False)
        result = self.my_deck.create_deck_cards()

        self.assertTrue(item in result)

if __name__ == '__main__':
    unittest.main()
