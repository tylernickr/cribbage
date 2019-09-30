from agents.randomagent import RandomAgent
from itertools import combinations
from rules import StandardRules


class BestHandAgent(RandomAgent):
    """
    This hand plays randomly with the exception of its initial hand selection.
    When placing crib cards down, the agent selects the highest scoring 4 cards
    to be in its hand, and places the other two cards down in the crib. This should
    be a significant improvement over a random agent.
    """

    def __init__(self):
        super(BestHandAgent, self).__init__()

    def place_crib_cards(self):
        best_combo = []
        best_score = -1
        for combo in combinations(self.hand, 4):
            hand_score = StandardRules.get_hand_score(combo, None)
            if hand_score > best_score:
                best_score = hand_score
                best_combo = combo

        crib_cards = []
        for i in range(len(self.hand)):
            if self.hand[i] not in best_combo:
                crib_cards.append(self.hand[i])
        self.hand = list(best_combo)

        return crib_cards
