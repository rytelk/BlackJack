import random;

# ----------------------------------------------------------------------------------------------------
class Card:
    def __init__(self, _figure, _color):
        self.figure = _figure;
        self.color = _color;
        return;

# ----------------------------------------------------------------------------------------------------
class Deck:
    def __init__(self):
        self.cards = [];
        for color in ["TREFL", "KARO", "KIER", "PIK"]:
            for figure in ([str(k) for k in range(2, 11)] + ["J", "Q", "K", "A"]):
                cards.append( Card(figure, color) );
        random.shuffle(self.cards);
        return;

    def getTopCard(self):
        if not self.cards:
            print("Deck is empty, error !");
            return;
        self.cards.pop();
        return;
# ----------------------------------------------------------------------------------------------------
