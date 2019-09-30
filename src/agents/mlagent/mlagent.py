from agents.baseagent import BaseAgent
from agents.mlagent.playagent import PlayAgent


class MLAgent(BaseAgent):
    # TODO: Implement

    def __init__(self):
        super(MLAgent, self).__init__()
        self.wins = 0
        self.play_agent = PlayAgent()

    def place_crib_cards(self):
        return [self.hand.pop(), self.hand.pop()]

    def play_card(self, cards):
        self.play_agent.play_card()

    def win(self):
        self.wins += 1

    def get_wins(self):
        return self.wins

    def lose(self):
        pass

    def new_round(self):
        self.play_agent.new_round()
