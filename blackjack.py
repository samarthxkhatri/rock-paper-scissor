import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10},
        ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        dealt_cards = []

        for _ in range(number):
            if self.cards:
                dealt_cards.append(self.cards.pop())

        return dealt_cards


class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            value += card.rank["value"]

            if card.rank["rank"] == "A":
                aces += 1

        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value

    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def display(self, show_all=False):
        print(f"\n{'Dealer' if self.dealer else 'Player'} Hand:")

        for index, card in enumerate(self.cards):
            if self.dealer and not show_all and index == 0:
                print("Hidden Card")
            else:
                print(card)

        if not self.dealer or show_all:
            print("Value:", self.get_value())


class Game:
    def check_winner(self, player_hand, dealer_hand):
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()

        if player_hand.is_blackjack() and dealer_hand.is_blackjack():
            print("Both have Blackjack! Push.")
            return True

        if player_hand.is_blackjack():
            print("Blackjack! You win!")
            return True

        if dealer_hand.is_blackjack():
            dealer_hand.display(show_all=True)
            print("Dealer has Blackjack! Dealer wins.")
            return True

        if player_value > 21:
            print("You busted! Dealer wins.")
            return True

        if dealer_value > 21:
            print("Dealer busted! You win.")
            return True

        return False

    def compare_hands(self, player_hand, dealer_hand):
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()

        print("\nFinal Results")
        print("-" * 30)

        player_hand.display(show_all=True)
        dealer_hand.display(show_all=True)

        if player_value > 21:
            print("You busted! Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busted! You win.")
        elif player_value > dealer_value:
            print("You win!")
        elif dealer_value > player_value:
            print("Dealer wins!")
        else:
            print("Push (Tie)!")

    def play(self):
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(
                    input("How many games do you want to play? ")
                )
            except ValueError:
                print("Please enter a valid number.")

        for game_number in range(1, games_to_play + 1):
            print("\n" + "*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            player_hand.add_card(deck.deal(2))
            dealer_hand.add_card(deck.deal(2))

            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            # Player turn
            while player_hand.get_value() < 21:
                choice = input("\nHit or Stand? (H/S): ").lower()

                while choice not in ["h", "hit", "s", "stand"]:
                    choice = input(
                        "Please enter Hit or Stand (H/S): "
                    ).lower()

                if choice in ["s", "stand"]:
                    break

                player_hand.add_card(deck.deal(1))
                player_hand.display()

                if player_hand.get_value() > 21:
                    break

            if player_hand.get_value() > 21:
                self.compare_hands(player_hand, dealer_hand)
                continue

            # Dealer turn
            print("\nDealer's turn...")
            dealer_hand.display(show_all=True)

            while dealer_hand.get_value() < 17:
                print("Dealer hits.")
                dealer_hand.add_card(deck.deal(1))
                dealer_hand.display(show_all=True)

            if dealer_hand.get_value() >= 17:
                print("Dealer stands.")

            self.compare_hands(player_hand, dealer_hand)


if __name__ == "__main__":
    game = Game()
    game.play()