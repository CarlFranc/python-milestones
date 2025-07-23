import unittest
from Milestone2BlackJack.Hand import Hand, calculate_ace_value
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
        expected_sum = 10
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_3_cards(self):
        expected_sum = 12
        self.my_hand.addCard(Card(Card.SPADES, Card.TWO, False))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_1_ace(self):
        expected_sum = 21
        self.my_hand.addCard(Card(Card.HEARTS, Card.ACE, redacted=False))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_1_ace_3_cards(self):
        expected_sum = 15
        self.my_hand.current_hand = list(map(lambda cards: (setattr(cards, 'redacted', False) or cards) if cards.redacted else cards, self.my_hand.current_hand))
        self.my_hand.addCard(Card(Card.HEARTS, Card.ACE, redacted=False))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_1_ace_3_cards_11(self):
        expected_sum = 18
        self.my_hand.clearHand()
        self.my_hand.addCard(Card(Card.CLUBS, Card.TWO, False))
        self.my_hand.addCard(Card(Card.SPADES, Card.FIVE, False))
        self.my_hand.addCard(Card(Card.DIAMONDS, Card.ACE, redacted=False))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_2_ace(self):
        expected_sum = 12
        self.my_hand.clearHand()
        self.my_hand.addCard(Card(Card.DIAMONDS, Card.ACE, redacted=False))
        self.my_hand.addCard(Card(Card.HEARTS, Card.ACE, redacted=False))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_get_sum_2_ace_1_redacted(self):
        expected_sum = 11
        self.my_hand.clearHand()
        self.my_hand.addCard(Card(Card.DIAMONDS, Card.ACE, redacted=False))
        self.my_hand.addCard(Card(Card.HEARTS, Card.ACE, redacted=True))
        self.assertEqual(expected_sum, self.my_hand.get_sum())

    def test_show_cards(self):
        player_name = 'Joey123'
        self.my_hand.addCard(Card(Card.CLUBS, Card.ACE, False))
        self.my_hand.show_cards(player_name)

    def test_show_cards_bust(self):
        player_name = 'Joey123'
        self.my_hand.addCard(Card(Card.HEARTS, Card.TEN, False))
        self.my_hand.addCard(Card(Card.DIAMONDS, Card.TEN, False))
        self.my_hand.show_cards(player_name)

    def test_show_redacted_card_new_sum(self):
        expected_sum = 14
        redacted_card = next((cards for cards in self.my_hand.current_hand if cards == Card(Card.DIAMONDS, Card.FOUR, True)), None)
        redacted_card.redacted = False
        new_sum = self.my_hand.get_sum()
        self.assertEqual(expected_sum, new_sum)

    def test_calculate_ace_1(self):
        expected = 1
        result = calculate_ace_value(other_card_sum = 20)
        self.assertEqual(expected, result)

    def test_calculate_ace_bust(self):
        expected = 0
        result = calculate_ace_value(other_card_sum = 21)
        self.assertEqual(expected, result)

    def test_calculate_ace_11(self):
        expected = 11
        result = calculate_ace_value(other_card_sum = 9)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
