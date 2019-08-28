from rules import StandardRules
from cards import Card


class TestRules(object):

    def test_card_scoring(self):
        card = [Card('5', 'H'), Card('5', 'D')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 2

        card = [Card('5', 'H'), Card('5', 'D'), Card('5', 'S')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 2

        card = [Card('4', 'H'), Card('5', 'D'), Card('6', 'S')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 5

        card = [Card('5', 'H'), Card('6', 'D'), Card('7', 'S')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 3

        card = [Card('4', 'H'), Card('4', 'D'), Card('4', 'S')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 0

        card = [Card('J', 'H'), Card('4', 'D'), Card('4', 'S')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 1

        card = [Card('4', 'H'), Card('7', 'H'), Card('Q', 'H'), Card('K', 'H'), Card('2', 'H')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 5

        card = [Card('4', 'H'), Card('7', 'H'), Card('Q', 'H'), Card('K', 'S'), Card('2', 'H')]
        up_card = Card('4', 'H')
        assert StandardRules.get_card_score(card, up_card) == 0

        card = [Card('4', 'S'), Card('7', 'H'), Card('Q', 'H'), Card('K', 'H'), Card('2', 'H')]
        up_card = Card('4', 'S')
        assert StandardRules.get_card_score(card, up_card) == 4
