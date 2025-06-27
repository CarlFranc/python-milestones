import copy
import unittest
from Milestone2BlackJack.Player import Player

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        initial_amt = 100.0
        cls.my_player = Player('Joey')
        cls.my_player.initialize_bankroll(initial_amt)

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
        my_player_copy = copy.deepcopy(self.my_player)
        self.assertEqual(expected, my_player_copy.bankroll_deduct(deduction_amt))

if __name__ == '__main__':
    unittest.main()
