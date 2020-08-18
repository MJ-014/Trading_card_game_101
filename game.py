from random import choice
from card import Card

class Deck:
    def __init__(self, cardNumber=5):
        self.cards = []
        for i in range(cardNumber):
            cardAdd = Card()
            cardAdd.chooseTypeRandomly()
            self.cards.append(cardAdd)

    def __add__(self, other):
        if type(other) == Card:
            self.cards.append(other)
        elif type(other) == Deck:
            self.cards += other.cards

yourDeck = Deck()

for i in yourDeck.cards:
    print(i.cardType)
