import random;

# ----------------------------------------------------------------------------------------------------
class Card:
    def __init__(self, _figure, _color, _value):
        self.figure = _figure;
        self.color = _color;
        self.value = _value
        return;

# ----------------------------------------------------------------------------------------------------
class Deck:
    def __init__(self, _usableAce):
        self.usableAce = _usableAce;
        self.cards = [];
    
        for i in range(4): # 4 decks of cards
            for color in ["TREFL", "KARO", "KIER", "PIK"]:
                for figure in ([str(k) for k in range(2, 11)]):
                    self.cards.append(Card(figure, color, int(figure)));
                for figure in ["J", "Q", "K"]:
                    self.cards.append(Card(figure, color, 10));
                self.cards.append(Card("A", color, 11))
        
        random.shuffle(self.cards);
        return;

    def GetTopCardValue(self):
        chosenCard = self.cards.pop()
        return chosenCard.value;
# ----------------------------------------------------------------------------------------------------
