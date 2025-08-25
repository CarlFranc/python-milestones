class Card:

    CLUBS       = {'SUIT': 'CLUBS', 'ICON': '\u2663'}
    SPADES      = {'SUIT': 'SPADES', 'ICON': '\u2660'}
    HEARTS      = {'SUIT': 'HEARTS', 'ICON': '\u2665'}
    DIAMONDS    = {'SUIT': 'DIAMONDS', 'ICON': '\u2666'}

    TWO     = {'RANK': '2' ,'VALUE': 2}
    THREE   = {'RANK': '3' ,'VALUE': 3}
    FOUR    = {'RANK': '4' ,'VALUE': 4}
    FIVE    = {'RANK': '5' ,'VALUE': 5}
    SIX     = {'RANK': '6' ,'VALUE': 6}
    SEVEN   = {'RANK': '7' ,'VALUE': 7}
    EIGHT   = {'RANK': '8' ,'VALUE': 8}
    NINE    = {'RANK': '9' ,'VALUE': 9}
    TEN     = {'RANK': '10' ,'VALUE': 10}
    JACK    = {'RANK': 'J' ,'VALUE': 10}
    QUEEN   = {'RANK': 'Q' ,'VALUE': 10}
    KING    = {'RANK': 'K' ,'VALUE': 10}
    ACE     = {'RANK': 'A' ,'VALUE': 11}

    SUITS_LIST = (CLUBS, SPADES, HEARTS, DIAMONDS)
    RANKS_LIST = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE)

    def __init__(self, suit, rank, redacted):
        self.suit = suit
        self.rank = rank
        self.redacted = redacted

    def __str__(self):
        if not self.redacted:
            return f'{self.rank['RANK']}({self.suit['ICON']})'
        return '?(?)'


    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank['VALUE'] == other.rank['VALUE'] and self.suit['SUIT'] == other.suit['SUIT'] and self.rank['RANK'] == other.rank['RANK'] and self.redacted == other.redacted
        return False




