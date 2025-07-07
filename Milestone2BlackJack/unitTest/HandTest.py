import unittest
from Milestone2BlackJack.Hand import Hand
from Milestone2BlackJack.Card import Card

class MyTestCase(unittest.TestCase):

    def setUp(self):
        card_jack_of_hearts = Card(Card.HEARTS, Card.JACK, False)
        card_four_of_diamond = Card(Card.DIAMONDS, Card.FOUR, True)
        self.my_hand = Hand(card_jack_of_hearts, card_four_of_diamond)


    def test_len_func(self):
        expected_hand_size = 2
        self.assertEqual(expected_hand_size, len(self.my_hand))

    def test_add_card(self):
        expected_hand_size = 3
        self.my_hand.addCard(Card(Card.CLUBS, Card.TEN, False))
        self.assertEqual(expected_hand_size, len(self.my_hand))

    def test_get_sum(self):
        expected_sum = 14
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_3_cards(self):
        expected_sum = 16
        self.my_hand.addCard(Card(Card.SPADES, Card.TWO, False))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_showcards(self):
        self.my_hand.addCard(Card(Card.CLUBS, Card.ACE, False))
        self.my_hand.show_cards()

if __name__ == '__main__':
    unittest.main()
