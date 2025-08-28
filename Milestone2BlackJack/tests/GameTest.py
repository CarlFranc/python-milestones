import unittest
from Milestone2BlackJack.Game import show_menu
from Milestone2BlackJack.Game import computer_action
from Milestone2BlackJack.components.Deck import Deck
from Milestone2BlackJack.components.Player import Player
from Milestone2BlackJack.components.Hand import Hand
from Milestone2BlackJack.components.Card import Card


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.playercomp = Player('test101')
        self.player1 = Player('player1test101')
        self.player1.bankroll = 100
        jack_of_hearts = Card(Card.HEARTS, Card.JACK, False)
        eight_of_clubs = Card(Card.CLUBS, Card.EIGHT, False)

        three_of_diamonds = Card(Card.DIAMONDS, Card.THREE, False)
        nine_of_spades = Card(Card.SPADES, Card.NINE, False)
        player_hand = Hand(three_of_diamonds, nine_of_spades)
        comp_hand = Hand(jack_of_hearts, eight_of_clubs)
        self.playercomp.set_hand(comp_hand)
        self.player1.set_hand(player_hand)

    def test_show_menu(self):
        show_menu()

    def test_computer_action_win(self):
        computer_action(self.deck.create_deck_cards(), self.player1, self.playercomp)

    def test_computer_action_hit(self):
        self.playercomp.hand.clearHand()
        two_of_hearts = Card(Card.HEARTS, Card.TWO, False)
        three_of_hearts = Card(Card.HEARTS, Card.THREE, False)
        self.playercomp.hand.addCard(two_of_hearts)
        self.playercomp.hand.addCard(three_of_hearts)
        computer_action(self.deck.create_deck_cards(), self.player1, self.playercomp)

    def test_computer_action_bust(self):
        king_of_hearts = Card(Card.HEARTS, Card.KING, False)
        jack_of_hearts = Card(Card.HEARTS, Card.JACK, False)
        self.playercomp.hand.addCard(king_of_hearts)
        self.playercomp.hand.addCard(jack_of_hearts)
        computer_action(self.deck.create_deck_cards(), self.player1, self.playercomp)

if __name__ == '__main__':
    unittest.main()
