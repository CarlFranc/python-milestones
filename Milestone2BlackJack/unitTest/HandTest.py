import unittest
from Milestone2BlackJack.Hand import Hand
from Milestone2BlackJack.Card import Card
from Milestone2BlackJack.Player import Player

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
        expected_sum = 10
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_3_cards(self):
        expected_sum = 12
        self.my_hand.addCard(Card(Card.SPADES, Card.TWO, False))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_showcards(self):
        player_name = 'Joey123'
        self.my_hand.addCard(Card(Card.CLUBS, Card.ACE, False))
        self.my_hand.show_cards(player_name)

    def test_show_redacted_card_new_sum(self):
        expected_sum = 14
        redacted_card = next((cards for cards in self.my_hand.current_hand if cards == Card(Card.DIAMONDS, Card.FOUR, True)), None)
        redacted_card.redacted = False
        new_sum = self.my_hand.get_sum()
        self.assertEqual(expected_sum, new_sum)

if __name__ == '__main__':
    unittest.main()
