class Board(object):
    GAME_SPACES = 120

    def __init__(self):
        self.p1position = self.__class__.GAME_SPACES
        self.p2position = self.__class__.GAME_SPACES

    def peg_p1(self, score):
        self.p1position -= score

    def peg_p2(self, score):
        self.p2position -= score
