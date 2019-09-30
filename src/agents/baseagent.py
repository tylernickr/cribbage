class BaseAgent(object):
    '''
    This is a class which other agents should extend. It enforces the methods
    that the game manager class expects to be present on its player agents.
    '''
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    def __init__(self):
        self.position = None
        self.hand = []

    def set_position(self, position):
        self.position = position

    def peg(self, board, spaces):
        if self.position == BaseAgent.PLAYER_ONE:
            board.peg_p1(spaces)
        else:
            board.peg_p2(spaces)

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def place_crib_cards(self):
        raise NotImplementedError("Agent must implement place_crib_cards method")

    def play_card(self, cards):
        raise NotImplementedError("Agent must implement play_card method")

    def new_round(self):
        raise NotImplementedError("Agent must implement new_round method")

    def win(self):
        raise NotImplementedError("Agent must implement win method")

    def lose(self):
        raise NotImplementedError("Agent must implement lose method")