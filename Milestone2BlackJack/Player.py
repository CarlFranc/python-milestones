class Player:

    def __init__(self, name):
        self.bankroll = 0.0
        self.name = name

    def __str__(self):
        return f'I am Player {self.name}'

    def initialize_bankroll(self, starting_amt):
        self.bankroll = starting_amt

    def bankroll_deduct(self, amount):
        try:
            self.bankroll -= amount
        except:
            print(f'Cannot deduct the specified amount on {self.name}\'s bankroll')
            return False
        else:
            return self.bankroll

    def set_hand(self, hand):
        self.hand = hand