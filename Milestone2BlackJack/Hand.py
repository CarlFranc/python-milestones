class Hand:

    def __init__(self, first_card, second_card, redacted_second_card):
        self.current_hand = []
        self.current_hand.append(first_card)
        self.current_hand.append(second_card)
        self.redacted_second_card = redacted_second_card

    def __len__(self):
        return len(self.current_hand)

    def addCard(self, new_card):
        self.current_hand.append(new_card)

    def clearHand(self):
        self.current_hand.clear()

    def get_sum(self):
        value = 0
        for cards in self.current_hand:
            value += cards.value

        return value

    def show_cards(self):
        for cards in self.current_hand:
            print("*".center(7, "*"))
            print(f"|{cards.value}({cards.suit_icons[cards.suit]})|")
            # TODO : Create show cards display


