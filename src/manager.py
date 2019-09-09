from board import Board
from rules import StandardRules
from cards import Deck


class GameManager(object):

    def __init__(self):
        self.board = None
        self.deck = None
        self.player1 = None
        self.player2 = None
        self.rounds = None

    def play(self):
        self.board = Board()
        self.rounds = 0
        self.player1.set_position(1)
        self.player2.set_position(2)
        while not self.victory():
            self.player1.new_round()
            self.player2.new_round()
            self.play_round()
            self.rounds += 1

    def play_round(self):
        self.deck = Deck.get_shuffled_deck()

        # Set the dealer for the round
        if self.rounds % 2 == 0:
            dealer = self.player1
            non_dealer = self.player2
        else:
            dealer = self.player2
            non_dealer = self.player1

        # Get player hands for the round
        for i in range(6):
            non_dealer.draw_card(self.deck)
            dealer.draw_card(self.deck)

        # Set the communal card
        up_card = self.deck.draw()
        dealer.peg(self.board, StandardRules.get_cut_jack_score(up_card))

        # Set the crib
        crib = non_dealer.place_crib_cards() + dealer.place_crib_cards()

    def victory(self):
        return StandardRules.p1_victory(self.board) or StandardRules.p2_victory(self.board)

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


if __name__ == '__main__':
    from agents.randomagent import RandomAgent
    game_manager = GameManager()
    game_manager.set_players(RandomAgent(), RandomAgent())
    game_manager.play()
