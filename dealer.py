from hand import Hand


class Dealer:
    def __init__(self):
        pass
        self.hand = Hand()

    def get_str_hand(self):
        return str(self.hand)

    def hit(self, deck):
        self.hand.add_card(deck.deal_card())
