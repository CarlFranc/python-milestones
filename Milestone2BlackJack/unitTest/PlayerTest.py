import unittest
from Milestone2BlackJack.Player import Player
from Milestone2BlackJack.Hand import Hand
from Milestone2BlackJack.Card import Card

class MyTestCase(unittest.TestCase):

    def setUp(self):
        initial_amt = 100.0
        jack_of_clubs = Card(Card.CLUBS, Card.JACK)
        king_of_hearts = Card(Card.HEARTS, Card.KING)
        self.my_player = Player('Joey', Hand(jack_of_clubs, king_of_hearts))
        self.my_player.initialize_bankroll(initial_amt)

    def testPlayerName(self):
        expected_name = 'Joey'
        self.assertEqual(expected_name, self.my_player.name)

    def testPlayerClassStr(self):
        expected = 'I am Player Joey'
        self.assertEqual(expected, str(self.my_player))

    def test_initialize_bankroll(self):
        expected = 100.0
        self.assertEqual(expected, self.my_player.bankroll)

    def testBankrollDeduction(self):
        expected = 80.0
        deduction_amt = 20.0
        self.assertEqual(expected, self.my_player.bankroll_deduct(deduction_amt))

if __name__ == '__main__':
    unittest.main()
