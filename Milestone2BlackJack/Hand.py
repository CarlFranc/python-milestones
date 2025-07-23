from Milestone2BlackJack.Card import Card

def calculate_ace_value(other_card_sum):
    ace_11 = (((11 + other_card_sum) <= 21) * 11) # 11
    ace_1 = (((1 + other_card_sum) <= 21 ) * 1) # 1

    if ace_1 == 0 and ace_11 == 0:
        # bust
        return 0

    return int(ace_11 if ace_11 > ace_1 else ace_1)

class Hand:

    def __init__(self, first_card, second_card):
        self.current_hand = []
        self.current_sum = 0
        self.current_hand.append(first_card)
        self.current_hand.append(second_card)
        self.get_sum()

    def __len__(self):
        return len(self.current_hand)

    def addCard(self, new_card):
        self.current_hand.append(new_card)
        self.get_sum()

    def clearHand(self):
        self.current_hand.clear()
        self.get_sum()

    def get_sum(self):
        value = 0
        aces_list = []
        for cards in self.current_hand:
            if not cards.redacted:
                if cards.rank['RANK'] == Card.ACE['RANK']:
                    aces_list.append(cards)
                else:
                    value += cards.rank['VALUE']

        for aces in aces_list:
            aces.rank['VALUE'] = calculate_ace_value(value)
            value += 1 if aces.rank['VALUE'] == 0 else aces.rank['VALUE']

        self.current_sum = value
        return value if value <= 21 else f'{value}(BUST!)'

    def show_cards(self, player_name):
        card_section_size = len(player_name) * len(self.current_hand)
        print(f'{player_name:-^{card_section_size}}')
        print(*self.current_hand, sep=' | ')
        print(f'{self.get_sum():-^{card_section_size}}')
