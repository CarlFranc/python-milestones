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
        for cards in self.current_hand:
            if not cards.redacted:
                value += cards.rank['VALUE']
        self.current_sum = value
        return value

    def show_cards(self, player_name):
        card_section_size = len(player_name) * len(self.current_hand)
        print(f'{player_name:-^{card_section_size}}')
        print(*self.current_hand, sep=' | ')
        print(f'{self.current_sum:-^{card_section_size}}')

    def check_bust(self):
        pass

    def calculate_ace_value(self, other_card_sum):
        ACE_11 = (((11 + other_card_sum) <= 21) * 11)
        ACE_1 = (((1 + other_card_sum) <= 21 ) * 1)

        if ACE_1 == 0 and ACE_11 == 0:
            # bust
            return 0

        return int((ACE_11 + ACE_1 + abs(ACE_11 - ACE_1)) / 2)
        # Case 1: 2 Aces

        # Case 3: only 1 Ace and both 1 and 11 less than 21