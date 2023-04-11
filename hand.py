from card import Card


class Hand:

    def __init__(self):
        self.cards = []

    def get_value(self):
        total = sum([card.value for card in self.cards])
        num_aces = sum([card.value == 1 for card in self.cards])
        for i in range(num_aces):
            if total + 10 <= 21:
                total += 10
        return total

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        card_strings = [str(card) for card in self.cards]
        return " ".join(card_strings)
