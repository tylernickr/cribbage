from random import randint
from rules import StandardRules
from agents.baseagent import BaseAgent


class RandomAgent(BaseAgent):
    """
    This agent makes random decision at all points that are within the rules of the game.
    """

    def __init__(self):
        super(RandomAgent, self).__init__()
        self.played_cards = []
        self.wins = 0

    def place_crib_cards(self):
        crib_cards = []
        for i in range(2):
            crib_cards.append(self.hand.pop(randint(0, len(self.hand) - 1)))
        return crib_cards

    def play_card(self, cards):
        tot_count = sum([StandardRules.get_numeric_card_value(card) for card in cards])
        playable_cards = [card for card in self.hand if card not in self.played_cards]
        playable_cards = [card for card in playable_cards if 31 - tot_count >= StandardRules.get_numeric_card_value(card)]
        if len(playable_cards) == 0:
            return None
        else:
            card_to_play = playable_cards.   pop(randint(0, len(playable_cards) - 1))
            self.played_cards.append(card_to_play)
            return card_to_play

    def new_round(self):
        self.hand = []
        self.played_cards = []

    def win(self):
        self.wins += 1

    def get_wins(self):
        return self.wins

    def lose(self):
        pass
