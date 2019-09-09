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
        if StandardRules.p1_victory(self.board):
            self.player1.win()
            self.player2.lose()
        else:
            self.player1.lose()
            self.player2.win()

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
        if self.victory():
            return

        # Set the crib
        crib = non_dealer.place_crib_cards() + dealer.place_crib_cards()

        # "The Play" phase
        last_card = None
        played_cards = []
        current_stack = []
        active_player = non_dealer
        inactive_player = dealer
        while len(played_cards) < 8:
            played_card = active_player.play_card(current_stack)
            if played_card is not None:
                played_cards.append(played_card)
                current_stack.append(played_card)
                if sum([StandardRules.get_numeric_card_value(card) for card in current_stack]) == 31:
                    active_player.peg(self.board, StandardRules.get_thirtyone_score())
                    if self.victory():
                        return
                    current_stack = []
            else:
                if last_card is None:
                    active_player.peg(self.board, StandardRules.get_last_card_score())
                    if self.victory():
                        return
                    current_stack = []

            last_card = played_card
            active_player, inactive_player = inactive_player, active_player

        # "The Show" phase
        non_dealer_hand = non_dealer.get_hand() + [up_card]
        dealer_hand = dealer.get_hand() + [up_card]
        crib_hand = crib + [up_card]
        non_dealer.peg(self.board, StandardRules.get_hand_score(non_dealer_hand, up_card))
        if self.victory():
            return
        dealer.peg(self.board, StandardRules.get_hand_score(dealer_hand, up_card))
        dealer.peg(self.board, StandardRules.get_hand_score(crib_hand, up_card))

    def victory(self):
        return StandardRules.p1_victory(self.board) or StandardRules.p2_victory(self.board)

    def set_players(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
