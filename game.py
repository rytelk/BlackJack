from deck import Deck
from game_result import GameResult

class Game:

    def __init__(self, usable_ace):
        self.dealer_cards = []
        self.player_cards = []
        self.deck = Deck(usable_ace)
        self.showing_card = None

    def play(self, start_check_limit):
        self.init_dealer_cards()
        self.init_player_cards()

        while self.get_player_cards_sum() < start_check_limit:
           self.player_cards.append(self.deck.GetTopCardValue(self.player_has_ace()))

        if self.get_player_cards_sum() > 21:
            win = 0
        if self.get_player_cards_sum() == 21:
            win = 1
        elif self.get_player_cards_sum() >= self.get_dealer_cards_sum():
            win = 1
        else:
            win = 0

        return GameResult(self.get_player_cards_sum(), self.showing_card, win)

    def init_dealer_cards(self):
        self.showing_card = self.deck.GetTopCardValue(False)
        self.dealer_cards.append(self.showing_card)
        self.dealer_cards.append(self.deck.GetTopCardValue(False))

    def init_player_cards(self):
        self.player_cards.append(self.deck.GetTopCardValue(self.player_has_ace()))
        self.player_cards.append(self.deck.GetTopCardValue(self.player_has_ace()))

    def get_player_cards_sum(self):
        return sum(self.player_cards)

    def get_dealer_cards_sum(self):
        return sum(self.dealer_cards)

    def player_has_ace(self):
        if 11 in self.player_cards:
            return True

        return False