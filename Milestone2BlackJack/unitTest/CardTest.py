import unittest
from Milestone2BlackJack.Card import Card

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_card = Card(Card.CLUBS, Card.JACK, False)

    def testSuit(self):
        expected_suit = 'CLUBS'
        self.assertEqual(expected_suit, self.my_card.suit['SUIT'])

    def testRank(self):
        expected_rank = 'J'
        self.assertEqual(expected_rank, self.my_card.rank['RANK'])

    def testStr(self):
        expected_string_alt = 'J(♣)'
        self.assertEqual(expected_string_alt, str(self.my_card))

    def test_value(self):
        expected_value = 10
        self.assertEqual(expected_value, self.my_card.rank['VALUE'])




if __name__ == '__main__':
    unittest.main()
