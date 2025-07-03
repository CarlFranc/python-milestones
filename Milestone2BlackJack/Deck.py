import random

from Milestone2BlackJack.Card import Card

class Deck:

    def __init__(self):
        pass

    def create_deck_cards(self):
        deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                deck.append(Card(suit, rank))

        random.shuffle(deck)
        return deck


