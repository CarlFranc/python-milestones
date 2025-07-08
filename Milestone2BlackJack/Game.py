from time import sleep

from Milestone2BlackJack.Deck import Deck
from Milestone2BlackJack.Player import Player
from Milestone2BlackJack.Hand import Hand

deck = Deck()
current_deck = deck.create_deck_cards()
comp_redacted_card = current_deck.pop()
comp_redacted_card.redacted = True
player_comp = Player('Computer', Hand(current_deck.pop(), comp_redacted_card))
player_1 = Player('Joey', Hand(current_deck.pop(), current_deck.pop()))
player_1.initialize_bankroll(1000)

print(f"{' Welcome to Black Jack Game ':-^50}")
# sleep(3)
print(f"{'CURRENT DECK':<15}{'.':.^26}{len(current_deck):>9}")
print(f"{'BANKROLL':<15}{'.':.^26}{player_1.bankroll:9,.2f}")

while True:
    try:
        bet_amt = float(input('BET? '))
    except:
        print('Bet amount is not valid.')
    else:
        if not (bet_amt <= 0 or bet_amt > player_1.bankroll):
            player_1.bankroll_deduct(bet_amt)
            break
        else:
            print('Bet amount is not valid!')

print('Showing cards...')
sleep(2)

player_comp.hand.show_cards(player_comp.name)
player_1.hand.show_cards(player_1.name)