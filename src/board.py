class Board(object):
    GAME_SPACES = 120

    def __init__(self):
        self.p1position = self.__class__.GAME_SPACES
        self.p2position = self.__class__.GAME_SPACES

    def peg_p1(self, score):
        self.p1position -= score

    def peg_p2(self, score):
        self.p2position -= score

    def get_p1_position(self):
        return self.p1position

    def get_p2_position(self):
        return self.p2position

    def __str__(self):
        result = ''
        result += 'Player 1: ' + str(self.p1position) + ', Player 2: ' + str(self.p2position)
        return result