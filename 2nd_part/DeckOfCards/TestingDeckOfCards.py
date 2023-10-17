import unittest
from DeckOfCards import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        self.assertEqual(repr(self.card), "A of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attribute which is list, and full decks are 52 length"""
        self.assertTrue(self.deck.cards, list)
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string with a form of 'Deck of {length} cards'"""
        self.assertEqual(repr(self.deck), f"Deck of 52 cards")

    def test_count(self):
        """count should return length of cards attribute"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_card(self):
        """deal_card should pop the last card in deck and repr it"""
        self.assertEqual(repr(self.deck.deal_card()), 'K of Spades')

    def test_deal_hand_sufficient(self):
        """deal_hand should pop the number of cards from the end and repr it"""
        dealt_cards = self.deck.deal_hand(10)
        self.assertEqual(len(dealt_cards), 10)
        self.assertEqual(len(self.deck.cards), 42)

    def test_deal_hand_more_length(self):
        """deal_hand should pop the maximum possible cards numbered and all if number > length"""
        self.deck.deal_hand(500)
        self.assertEqual(len(self.deck.cards), 0)

    def test_deal_no_cards(self):
        """deal_no_cards should raise ValueError if you deal cards while there's no cards in deck"""
        self.deck.deal_hand(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck.deal_card()

    def test_shuffle(self):
        """shuffle should only shuffle cards in deck"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), len(cards))

    def test_shuffle_insufficient(self):
        """shuffle should raise ValueError if deck is not full"""
        self.deck.cards.pop()
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == "__main__":
    unittest.main()
