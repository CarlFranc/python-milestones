import os
from time import sleep

from Milestone2BlackJack.Deck import Deck
from Milestone2BlackJack.Player import Player
from Milestone2BlackJack.Hand import Hand

def initialize_deck():
    deck = Deck()
    return deck.create_deck_cards()

def initialize_player(bankroll_init):
    if bankroll_init:
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
    while player_1.hand.current_sum <= 21:
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
                if player_1.hand.current_sum > 21:
                    print('YOU LOSE')
                    break
            elif player_choice == 2:
                os.system('cls')
            else:
                print('Invalid choice!')
                break

def show_menu():
    global initialize_bankroll
    while True:
        try:
            print(f'{' GAME OVER ':-^48}')
            print(f'{'CONTINUE (1)':<16}{'RESTART GAME (2)':^16}{'QUIT (3)':>16}')
            user_choice = int(input('Choose: '))
        except:
            print('Invalid choice!')
        else:
            if user_choice == 1:
                os.system('cls')
                if player_1.bankroll <= 0:
                    print(f'Not enough money to continue')
                else:
                    initialize_bankroll = False
                    break
            elif user_choice == 2:
                os.system('cls')
                initialize_bankroll = True
                break
            elif user_choice == 3:
                print('Bye')
                exit(0)
            else:
                print('Invalid choice!')

if __name__ == '__main__':
    current_deck = []
    default_initial_bankroll = 1000.0
    player_comp = Player('Computer')
    player_1 = Player('Joey11')
    player_current_bet = 0.0
    initialize_bankroll = True

    while True:
        current_deck = initialize_deck()
        player_1 = initialize_player(initialize_bankroll)
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
        show_menu()