from Milestone2BlackJack.components.Deck import Deck
from Milestone2BlackJack.components.Card import Card

class TestDeckModule():
    my_deck = Deck()

    def test_create_deck_full_size(self):
        expected_size = 52
        result = self.my_deck.create_deck_cards()
        assert  len(result) == expected_size

    def test_create_deck_contents(self):
        item = Card(Card.DIAMONDS, Card.EIGHT, False)
        result = self.my_deck.create_deck_cards()
        assert item in result
