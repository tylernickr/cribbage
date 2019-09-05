from rules import StandardRules
from cards import Card


class TestRules(object):

    def test_hand_scoring(self):
        card = [Card('4', 'H'), Card('7', 'H'), Card('Q', 'H'), Card('K', 'H'), Card('2', 'H')]
        up_card = Card('4', 'H')
        assert StandardRules.get_hand_score(card, up_card) == 5

        card = [Card('4', 'H'), Card('7', 'H'), Card('Q', 'H'), Card('K', 'S'), Card('2', 'H')]
        up_card = Card('4', 'H')
        assert StandardRules.get_hand_score(card, up_card) == 0

        card = [Card('4', 'S'), Card('7', 'H'), Card('Q', 'H'), Card('K', 'H'), Card('2', 'H')]
        up_card = Card('4', 'S')
        assert StandardRules.get_hand_score(card, up_card) == 4

        card = [Card('5', 'S'), Card('5', 'C'), Card('5', 'D'), Card('5', 'H'), Card('J', 'S')]
        up_card = Card('5', 'S')
        assert StandardRules.get_hand_score(card, up_card) == 29
