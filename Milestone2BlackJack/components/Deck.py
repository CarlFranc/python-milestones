import random

from .Card import Card

class Deck:

    def __init__(self):
        pass

    def create_deck_cards(self):
        deck = []
        for suit in Card.SUITS_LIST:
            for rank in Card.RANKS_LIST:
                deck.append(Card(suit, rank, False))

        random.shuffle(deck)
        return deck


