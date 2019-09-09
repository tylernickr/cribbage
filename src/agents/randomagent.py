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

    def set_position(self, position):
        self.position = position

    def peg(self, board, spaces):
        if self.position == RandomAgent.PLAYER_ONE:
            board.peg_p1(spaces)
        else:
            board.peg_p2(spaces)