from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ("Hearts", "Diamonds", "Clubs", "Spades")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        length = self.count()
        actual = min([length, number])
        if length == 0:
            raise ValueError("All cards have been dealt")
        dealt_cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return dealt_cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)
