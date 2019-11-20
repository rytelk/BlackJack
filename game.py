from deck import Deck
from game_result import GameResult

class Game:
    def __init__(self, usable_ace):
        self.dealer_cards = []
        self.player_cards = []

        self.player_sum = 0
        self.dealer_sum = 0
        self.usable_ace = usable_ace

        self.deck = Deck(self.usable_ace)
        self.showing_card = None

    def play(self, start_check_limit):
        self.init_dealer_cards() # two cards for dealer
        self.init_player_cards() # two cards for player

        if(self.get_player_cards_sum() == 21):
            # natural when dealer also has 21
            win = 0 if self.get_dealer_cards_sum() == 21 else 1
            return GameResult(self.get_player_cards_sum(), self.showing_card, win)
        
        # player hitting until stopping
        while self.get_player_cards_sum() < start_check_limit:
            self.add_card(self.deck.GetTopCardValue(), self.player_cards)

        # bust, instant lose
        if self.get_player_cards_sum() > 21:
            return GameResult(self.get_player_cards_sum(), self.showing_card, -1)

        # dealer's turn
        while self.get_dealer_cards_sum() < 17:
            self.add_card(self.deck.GetTopCardValue(), self.dealer_cards)

        if self.get_player_cards_sum() > 21:
            win = -1
        elif self.get_dealer_cards_sum() > 21:
            win = 1
        elif self.get_player_cards_sum() == 21:
            win = 1
        elif self.get_dealer_cards_sum() == self.get_player_cards_sum():
            win = 0
        elif self.get_player_cards_sum() > self.get_dealer_cards_sum():
            win = 1
        else:
            win = -1

        return GameResult(self.get_player_cards_sum(), self.showing_card, win)

    def init_dealer_cards(self):
        self.showing_card = self.deck.GetTopCardValue()
        
        self.add_card(self.showing_card, self.dealer_cards)
        self.add_card(self.deck.GetTopCardValue(), self.dealer_cards)

    def init_player_cards(self):
        self.add_card(self.deck.GetTopCardValue(), self.player_cards)
        self.add_card(self.deck.GetTopCardValue(), self.player_cards)

    def add_card(self, card_value, collection):
        collection.append(card_value)

    def get_total_value(self, collection, usable_ace):
        totalSum = sum(collection)

        if self.usable_ace and totalSum > 21 and 11 in collection:
            totalSum = totalSum - collection.count(11) * 10

        return totalSum

    def get_player_cards_sum(self):
        return self.get_total_value(self.player_cards, self.usable_ace)

    def get_dealer_cards_sum(self):
        return self.get_total_value(self.dealer_cards, self.usable_ace)
