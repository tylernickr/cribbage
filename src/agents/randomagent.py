from random import randint


class RandomAgent(object):
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    def __init__(self):
        self.hand = []
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

    def new_round(self):
        self.hand = []
        self.position = None