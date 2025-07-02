class Card:

    CLUBS = 'CLUBS'
    SPADES = 'SPADES'
    HEARTS = 'HEARTS'
    DIAMONDS = 'DIAMONDS'

    CLUBS_ICON = '\u2663'
    SPADES_ICON = '\u2660'
    HEARTS_ICON = '\u2665'
    DIAMONDS_ICON = '\u2666'

    suit_icons = {
        CLUBS: CLUBS_ICON,
        SPADES: SPADES_ICON,
        HEARTS: HEARTS_ICON,
        DIAMONDS: DIAMONDS_ICON
    }

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10
    ACE = 11 # OR 1

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}({self.suit_icons[self.suit]})'


