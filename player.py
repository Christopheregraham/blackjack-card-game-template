from hand import Hand


class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = Hand()

    def get_str_hand(self):
        return str(self.hand)

    def get_balance(self):
        return self.balance
