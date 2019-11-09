import random;

# ----------------------------------------------------------------------------------------------------
class Card:
    def __init__(self, _figure, _color):
        self.figure = _figure;
        self.color = _color;
        return;

# ----------------------------------------------------------------------------------------------------
class Deck:
    def __init__(self, _usableAce):
        self.usableAce = _usableAce;
        self.cards = [];
        for color in ["TREFL", "KARO", "KIER", "PIK"]:
            for figure in ([str(k) for k in range(2, 11)] + ["J", "Q", "K", "A"]):
                cards.append( Card(figure, color) );
        random.shuffle(self.cards);
        return;

    def GetTopCardValue(self, player_second_ace):
        topCardFigure = self.cards[-1].figure;
        topCardValue = 0;
        
        if topCardFigure == "A":
            if self.usableAce and player_second_ace:
                topCardValue = 1;
            else:
                topCardValue = 11;
        elif topCardFigure in ["J", "Q", "K"]:
            topCardValue = 10;
        else:
            topCardValue = int(topCardFigure);
        
        self.cards.pop();
        return topCardValue;
# ----------------------------------------------------------------------------------------------------
