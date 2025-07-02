class Hand:

    def __init__(self, first_card, second_card):
        self.current_hand = []
        self.current_hand.append(first_card)
        self.current_hand.append(second_card)

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

