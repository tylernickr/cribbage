from itertools import combinations


class StandardRules(object):

    class Messages(object):
        INVALID_CARD = "Card is not a valid cribbage card"

    @staticmethod
    def get_numeric_card_value(card):
        try:
            return int(card.get_value())
        except:
            if card.get_value() in ['J', 'Q', 'K']:
                return 10
            elif card.get_value() == 'A':
                return 1
            else:
                raise RuntimeError(StandardRules.Messages.INVALID_CARD + ': ' + str(card))

    @staticmethod
    def get_card_order_value(card):
        try:
            return int(card.get_value())
        except:
            order_map = { 'J': 11, 'Q': 12, 'K': 13, 'A': 1}
            try:
                return order_map[card.get_value()]
            except:
                raise RuntimeError(StandardRules.Messages.INVALID_CARD + ': ' + str(card))

    @staticmethod
    def get_hand_score(cards, up_card):
        score = 0
        score += StandardRules.get_pair_score(cards)
        score += StandardRules.get_run_score(cards)
        score += StandardRules.get_fifteen_score(cards)
        score += StandardRules.get_flush_score(cards, up_card)
        score += StandardRules.get_rjack_score(cards, up_card)
        return score

    @staticmethod
    def get_pair_score(cards):
        return StandardRules.get_pair_count(cards) * 2

    @staticmethod
    def get_pair_count(cards):
        pair_count = 0
        for i in range(len(cards)):
            first_card = cards[i]
            remaining_cards = cards[i+1:]
            for second_card in remaining_cards:
                if first_card.get_value() == second_card.get_value():
                    pair_count += 1
        return pair_count

    @staticmethod
    def get_run_score(cards):
        longest_run = 0
        current_run = 0
        card_values = [StandardRules.get_card_order_value(card) for card in cards]
        card_values.sort()
        for i in range(len(card_values)-1):
            current_card_val = card_values[i]
            next_card_val = card_values[i+1]
            if next_card_val - current_card_val == 1:
                current_run += 1
                longest_run = max(longest_run, current_run)
            else:
                current_run = 0
        if longest_run > 2:
            return longest_run
        else:
            return 0

    @staticmethod
    def get_fifteen_score(cards):
        all_card_combos = []
        for i in range(2, len(cards)+1):
            for combo in combinations(cards, i):
                all_card_combos.append(combo)
        score = 0
        for combo in all_card_combos:
            if sum([StandardRules.get_numeric_card_value(card) for card in combo]) == 15:
                score += 2
            else:
                score += 0
        return score

    @staticmethod
    def get_flush_score(cards, up_card):
        cards = [card for card in cards if card != up_card]  # Exclude up card
        for i in range(0, len(cards)-1):
            first_card = cards[i]
            second_card = cards[i+1]
            if first_card.get_suit() != second_card.get_suit():
                return 0
        if up_card.get_suit() == cards[0].get_suit():
            return 5
        else:
            return 4

    @staticmethod
    def get_rjack_score(cards, up_card):
        for card in [card for card in cards if card != up_card]:
            if card.get_value() == 'J' and card.get_suit() == up_card.get_suit():
                return 1
        return 0


