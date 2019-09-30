class PlayAgent(object):

    def __init__(self):
        self.hand = []
        self.played_cards = []

    def play_card(self):
        pass

    def set_hand(self, hand):
        self.hand = hand

    def new_round(self):
        self.hand = []
        self.played_cards = []