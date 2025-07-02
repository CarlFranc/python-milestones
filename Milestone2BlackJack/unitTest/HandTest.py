import unittest
from Milestone2BlackJack.Hand import Hand
from Milestone2BlackJack.Card import Card

class MyTestCase(unittest.TestCase):

    def setUp(self):
        card_eight_of_hearts = Card(Card.HEARTS, Card.EIGHT)
        card_two_of_diamond = Card(Card.DIAMONDS, Card.TWO)
        self.my_hand = Hand(card_eight_of_hearts, card_two_of_diamond)


    def test_len_func(self):
        expected_hand_size = 2
        self.assertEqual(expected_hand_size, len(self.my_hand))

    def test_add_card(self):
        expected_hand_size = 3
        self.my_hand.addCard(Card(Card.CLUBS, Card.TEN))
        self.assertEqual(expected_hand_size, len(self.my_hand))

    def test_get_sum(self):
        expected_sum = 10
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_3_cards(self):
        expected_sum = 19
        self.my_hand.addCard(Card(Card.SPADES, Card.NINE))
        self.assertEqual(expected_sum, self.my_hand.get_sum())


if __name__ == '__main__':
    unittest.main()
