from Milestone2BlackJack.components.Player import Player
from Milestone2BlackJack.components.Hand import Hand
from Milestone2BlackJack.components.Card import Card

class TestPlayerModule:

    def setup_method(self):
        initial_amt = 100.0
        jack_of_clubs = Card(Card.CLUBS, Card.JACK, False)
        king_of_hearts = Card(Card.HEARTS, Card.KING, False)
        self.my_player = Player('Joey')
        self.my_player.set_hand(Hand(jack_of_clubs, king_of_hearts))
        self.my_player.initialize_bankroll(initial_amt)

    def test_player_name(self):
        expected_name = 'Joey'
        assert self.my_player.name == expected_name

    def test_player_class_str(self):
        expected = 'I am Player Joey'
        assert str(self.my_player) == expected

    def test_initialize_bankroll(self):
        expected = 100.0
        assert self.my_player.bankroll == expected

    def test_bankroll_deduction(self):
        expected = 80.0
        deduction_amt = 20.0
        assert self.my_player.bankroll_deduct(deduction_amt) == expected

