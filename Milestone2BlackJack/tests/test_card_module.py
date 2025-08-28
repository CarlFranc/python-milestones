from Milestone2BlackJack.components.Card import Card

class TestCardModule:
    my_card = Card(Card.CLUBS, Card.JACK, False)

    def test_suit(self):
        expected_suit = 'CLUBS'
        assert self.my_card.suit['SUIT'] == expected_suit

    def test_rank(self):
        expected_rank = 'J'
        assert self.my_card.rank['RANK'] == expected_rank

    def test_str(self):
        expected_string_alt = 'J(♣)'
        assert str(self.my_card) == expected_string_alt

    def test_value(self):
        expected_value = 10
        assert self.my_card.rank['VALUE'] == expected_value