import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["♠", "♡", "♢", "♣"]
        self.ranks = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                      "7": 7, "8": 8, "9": 9, "T": 10, "K": 10, "Q": 10, "J": 10, "A": 11}

        self.create_deck()

    def create_deck(self):
        for suit in Card.SUIT_SYMBOLS:
            for rank in Card.VALUE_NAMES:
                card = Card(suit, rank)
                card.suit = Card.SUIT_SYMBOLS[suit]
                card.rank = Card.VALUE_NAMES[rank]
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
