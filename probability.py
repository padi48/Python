import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in ["Spades", "Clubs", "Diamds", "Hearts"]:
            for f in range(1, 14):
                self.cards.append(Card(i, f))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rn = random.randint(0, i)
            self.cards[i], self.cards[rn] = self.cards[rn], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck) :
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


deck = Deck()
deck.shuffle()
deck.show()

matt = Player("Matthew")
matt.draw(deck).draw(deck)
matt.showHand()
