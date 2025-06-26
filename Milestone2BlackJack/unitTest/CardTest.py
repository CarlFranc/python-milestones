import unittest
from Milestone2BlackJack.Card import Card

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_card = Card(Card.CLUBS, Card.EIGHT)

    def testSuit(self):
        expected_suit = 'CLUBS'
        self.assertEqual(expected_suit, self.my_card.suit)

    def testRank(self):
        expected_rank = 8
        self.assertEqual(expected_rank, self.my_card.rank)

    def testStr(self):
        expected_string = '8 of CLUBS'
        self.assertEqual(expected_string, str(self.my_card))

if __name__ == '__main__':
    unittest.main()
