from Milestone2BlackJack.Game import computer_action, validate_user_bet_input, player_1, \
    player_comp, player_hit, show_all_cards
from Milestone2BlackJack.components.Player import Player
import Milestone2BlackJack.Game
from Milestone2BlackJack.components.Hand import Hand
from Milestone2BlackJack.components.Card import Card
import pytest

class TestGameModule:

    TEST_BANKROLL = 200
    TEST_BET_AMT = 123
    COMPUTER = 'COMPUTER'
    HUMAN = 'HUMAN'

    @pytest.fixture
    def mock_user_input_string(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "abc")

    @pytest.fixture
    def mock_user_input_float(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: str(self.TEST_BET_AMT))

    @pytest.fixture
    def mock_user_input_exceed_bankroll(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1000")

    @pytest.fixture
    def mock_bankroll(self, monkeypatch):
        monkeypatch.setattr(player_1, 'bankroll', self.TEST_BANKROLL)

    @pytest.fixture
    def patch_hand_add_card(self, monkeypatch):
        test_card_1 = Card(Card.CLUBS, Card.TWO, redacted=False)
        test_card_2 = Card(Card.CLUBS, Card.THREE, redacted=False)
        monkeypatch.setattr(player_1.hand, 'current_hand', [test_card_1, test_card_2])
        monkeypatch.setattr(player_1.hand, 'addCard', lambda _: None)

    @pytest.fixture
    def patch_show_banner(self, monkeypatch):
        monkeypatch.setattr(Milestone2BlackJack.Game,'show_banner', None)

    @pytest.fixture
    def patch_screen_prints(self, monkeypatch):
        monkeypatch.setattr(Milestone2BlackJack.Game, 'clear_screen', lambda: None)
        monkeypatch.setattr(player_comp.hand, 'show_cards', lambda x: None)
        monkeypatch.setattr(Milestone2BlackJack.Game, 'show_banner', lambda x, y: None)

    @pytest.mark.parametrize('card1,card2,result', [
        (Card(Card.CLUBS, Card.SEVEN, False), Card(Card.HEARTS, Card.THREE,False), True),
        (Card(Card.CLUBS, Card.JACK, False), Card(Card.HEARTS, Card.QUEEN, False), False)
    ])
    def test_player_hit_below_21(self,card1,card2,result,patch_screen_prints,monkeypatch):
        card_1 = Card(Card.CLUBS, Card.SEVEN, redacted=False)
        card_2 = Card(Card.HEARTS, Card.TWO, redacted=False)

        test_hand = Hand(card1, card2)

        monkeypatch.setattr(player_1, 'hand', test_hand)
        monkeypatch.setattr(Milestone2BlackJack.Game, 'current_deck', [card_1, card_2])

        monkeypatch.setattr(player_1.hand, 'show_cards', lambda x: None)
        player_hit_result = player_hit()
        assert player_hit_result == result

    @pytest.fixture
    def test_cards_initial(self):
        card_1 = Card(Card.CLUBS, Card.SEVEN, redacted=False)
        card_2 = Card(Card.CLUBS, Card.TWO, redacted=True)
        return Hand(card_1, card_2)

    def test_take_player_bet_value_error_exception(self, mock_user_input_string, mock_bankroll, capsys):
        result = validate_user_bet_input()
        out = capsys.readouterr()
        assert 'could not convert string to float' in str(out)
        assert result is None

    def test_take_player_bet_positive(self, monkeypatch, mock_user_input_float, mock_bankroll):
        result = validate_user_bet_input()
        assert result == 123
        assert player_1.bankroll == (self.TEST_BANKROLL - self.TEST_BET_AMT)

    def test_take_player_bet_negative(self, mock_user_input_exceed_bankroll, mock_bankroll, capsys):
        result = validate_user_bet_input()
        out = capsys.readouterr()
        assert 'Invalid bet amount!' in str(out)
        assert result is None

    def test_show_all_cards(self, test_cards_initial):
        hand_cards = show_all_cards(test_cards_initial)
        for cards in hand_cards:
            assert cards.redacted is False

    @pytest.mark.parametrize('p_card_1,p_card_2, c_card_1, c_card_2,result', [
        (Card(Card.HEARTS, Card.FOUR, False), Card(Card.CLUBS, Card.SEVEN, False), Card(Card.CLUBS, Card.NINE, False), Card(Card.SPADES, Card.JACK, True), "Computer wins"),
        (Card(Card.HEARTS, Card.NINE, False), Card(Card.CLUBS, Card.SIX, False), Card(Card.CLUBS, Card.FOUR, False),Card(Card.HEARTS, Card.QUEEN, True), "Computer busts, you win!")
    ])
    def test_computer_action_win(self, monkeypatch,capsys, p_card_1,p_card_2, c_card_1, c_card_2,result):
        def fake_sleep():
            pass

        def fake_deck_of_cards() -> list[Card]:
            t_card_1 = Card(Card.CLUBS, Card.KING, False)
            t_card_2 = Card(Card.SPADES, Card.QUEEN, False)
            t_card_3 = Card(Card.HEARTS, Card.JACK, False)

            return [t_card_1, t_card_2, t_card_3]

        self.player_computer = Player(self.COMPUTER)
        self.player_human = Player(self.HUMAN)
        self.player_human.bankroll = self.TEST_BANKROLL

        test_card_1 = p_card_1
        test_card_2 = p_card_2
        test_card_3 = c_card_1
        test_card_4 = c_card_2

        player_computer_hand = Hand(test_card_3, test_card_4)
        player_human_hand = Hand(test_card_1, test_card_2)

        self.player_human.set_hand(player_human_hand)
        self.player_computer.set_hand(player_computer_hand)

        monkeypatch.setattr(Milestone2BlackJack.Game, 'show_banner', lambda x, y: None)
        monkeypatch.setattr(player_computer_hand, 'show_cards', lambda x: None)
        monkeypatch.setattr(player_human_hand, 'show_cards', lambda x: None)
        monkeypatch.setattr(Milestone2BlackJack.Game, 'clear_screen', lambda : None)
        monkeypatch.setattr('time.sleep', fake_sleep)

        computer_action(fake_deck_of_cards(), self.player_human, self.player_computer)
        out = capsys.readouterr()
        assert result in str(out)