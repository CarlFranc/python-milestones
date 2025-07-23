import os
from time import sleep

from Milestone2BlackJack.Deck import Deck
from Milestone2BlackJack.Player import Player
from Milestone2BlackJack.Hand import Hand

current_deck = []
default_initial_bankroll = 1000.0
player_comp = Player('Computer')
player_1 = None
player_current_bet = 0.0

def initialize_deck():
    deck = Deck()
    return deck.create_deck_cards()

def initialize_player():
    player_1 = Player('Joey')
    player_1.initialize_bankroll(default_initial_bankroll)
    return player_1

def show_banner(player, deck):
    print(f"{' Welcome to Black Jack Game ':-^50}")
    sleep(2)
    print(f"{'CURRENT DECK':<15}{'.':.^26}{len(deck):>9}")
    print(f"{'BANKROLL':<15}{'.':.^26}{player.bankroll:9,.2f}")

def take_player_bet():
    while True:
        try:
            bet_amt = float(input('BET? '))
        except:
            print('Invalid bet amount!')
        else:
            if not (bet_amt <= 0 or bet_amt > player_1.bankroll):
                player_1.bankroll_deduct(bet_amt)
                return bet_amt
            else:
                print('Invalid bet amount!')

def player_hit_or_stay_prompt():
    while True:
        try:
            player_choice = int(input('Hit(1) or Stay(2)?: '))
        except:
            print('Invalid choice!')
        else:
            if player_choice == 1:
                os.system('cls')
                player_1.hand.addCard(current_deck.pop())
                show_banner(player_1, current_deck)
                player_comp.hand.show_cards(player_comp.name)
                player_1.hand.show_cards(player_1.name)
                break
            elif player_choice == 2:
                pass
            else:
                print('Invalid choice!')



current_deck = initialize_deck()
player_1 = initialize_player()
show_banner(player_1, current_deck)

player_current_bet = take_player_bet()

print('Dealing cards...')
sleep(2)
comp_redacted_card = current_deck.pop()
comp_redacted_card.redacted = True
player_comp.set_hand(Hand(current_deck.pop(), comp_redacted_card))
player_1.set_hand(Hand(current_deck.pop(), current_deck.pop()))

player_comp.hand.show_cards(player_comp.name)
player_1.hand.show_cards(player_1.name)
player_hit_or_stay_prompt()