from random import randint
from rules import StandardRules


class RandomAgent(object):
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    def __init__(self):
        self.hand = []
        self.played_cards = []
        self.position = None

    def draw_card(self, deck):
        self.hand.append(deck.draw())

    def get_hand(self):
        return self.hand

    def place_crib_cards(self):
        crib_cards = []
        for i in range(2):
            crib_cards.append(self.hand.pop(randint(0, len(self.hand) - 1)))
        return crib_cards

    def set_position(self, position):
        self.position = position

    def peg(self, board, spaces):
        if self.position == RandomAgent.PLAYER_ONE:
            board.peg_p1(spaces)
        else:
            board.peg_p2(spaces)

    def play_card(self, cards):
        tot_count = sum([StandardRules.get_numeric_card_value(card) for card in cards])
        playable_cards = [card for card in self.hand if card not in self.played_cards]
        playable_cards = [card for card in playable_cards if 31 - tot_count >= StandardRules.get_numeric_card_value(card)]
        if len(playable_cards) == 0:
            return None
        else:
            card_to_play = playable_cards.pop(randint(0, len(playable_cards) - 1))
            self.played_cards.append(card_to_play)
            return card_to_play

    def new_round(self):
        self.hand = []
        self.played_cards = []
