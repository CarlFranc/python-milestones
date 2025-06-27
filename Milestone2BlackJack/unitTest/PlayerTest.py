import unittest
from Milestone2BlackJack.Player import Player


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_player = Player('Joey')

    def testPlayerName(self):
        expected_name = 'Joey'
        self.assertEqual(expected_name, self.my_player.name)

    def testPlayerClassStr(self):
        expected = 'I am Player Joey'
        self.assertEqual(expected, str(self.my_player))

if __name__ == '__main__':
    unittest.main()
