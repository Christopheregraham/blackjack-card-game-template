from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.deck = None

    def start_game(self):
        print("Welcome to Blackjack!")
        print(f"Your current balance is ${self.player.get_balance()}")
        while self.player.get_balance() >= self.MINIMUM_BET:
            while True:
                self.bet = input(
                    f"Enter a bet of ${self.MINIMUM_BET} or more: ")
                try:
                    self.bet = int(self.bet)
                    if self.bet < self.MINIMUM_BET:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid bet, please try again.")
            print(f"You have bet ${self.bet}.")
            self.deck = Deck()
            self.deck.shuffle()
            self.player.hand = Hand()
            self.player.hand.add_card(self.deck.deal_card())
            self.player.hand.add_card(self.deck.deal_card())
            self.dealer.hand = Hand()
            self.dealer.hand.add_card(self.deck.deal_card())
            self.dealer.hand.add_card(self.deck.deal_card())
            print("Dealer's up card is:", self.dealer.get_str_handh())
            while True:
                print("Your hand is:", self.player.get_str_hand(),
                      "Your score is:", self.player.hand.get_value())
                hit_or_stand = input("Do you want to hit or stand? ")
                if hit_or_stand.lower() == "hit":
                    new_card = self.deck.deal_card()
                    self.player.hand.add_card(new_card)
                    print(
                        f"You have been dealt {new_card} current hand score:", self.player.hand.get_value())
                    if self.player.hand.get_value() == 21:
                        print(f"Blackjack! You win ${self.bet * 1.5} :)")
                        self.player.balance += (self.bet * 1.5)
                        break
                    elif self.player.hand.get_value() > 21:
                        print(
                            f"Your hand value is over 21 and you lose ${self.bet} :(")
                        self.player.balance -= self.bet
                        break
                elif hit_or_stand.lower() == "stand":
                    while self.dealer.hand.get_value() < 17:
                        self.dealer.hit(self.deck)
                    print("Dealer's new hand is:", self.dealer.get_str_hand())
                    if self.dealer.hand.get_value() > 21:
                        print("Dealer bust! You win.")
                        self.player.balance += self.bet
                        break
                    elif self.player.hand.get_value() > self.dealer.hand.get_value():
                        print("You win!")
                        self.player.balance += self.bet
                        break
                    elif self.player.hand.get_value() < self.dealer.hand.get_value():
                        print("You lose.")
                        self.player.balance -= self.bet
                        break
                    else:
                        print("Push (tie).")
                        break
                else:
                    print("Invalid input, please try again.")
            print(f"Your balance is now ${self.player.get_balance()}.")
        print("Game over. You are out of money.")
