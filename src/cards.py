from random import shuffle


class Deck(object):
    CARD_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    CARD_SUITS = ['H', 'D', 'S', 'C']

    @staticmethod
    def get_shuffled_deck():
        deck = Deck()
        deck.shuffle()
        return deck

    def __init__(self):
        self.cards = []
        for cardSuit in self.__class__.CARD_SUITS:
            for cardValue in self.__class__.CARD_VALUES:
                self.cards.append(Card(cardValue, cardSuit))

    def shuffle(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Card(object):

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def __str__(self):
        return self.value + self.suit

    def __eq__(self, other):
        try:
            return self.get_value() + self.get_suit() == other.get_value() + other.get_suit()
        except AttributeError:
            return False
