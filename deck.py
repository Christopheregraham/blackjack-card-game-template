import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        for suit in Card.SUIT_SYMBOLS:
            for rank in Card.VALUE_NAMES.values():
                card = Card(suit, rank)
                card.suit = Card.SUIT_SYMBOLS[suit]
                card.rank = rank
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
