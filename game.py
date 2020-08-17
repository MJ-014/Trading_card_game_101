from random import choice
from card import Card

class Deck:
    def __init__(self, deckType=0):
        self.cards = []
        if deckType == 1:
            for i in range(5):
                card = Card()
                self.cards.append(card)
        self.deckType = deckType

    def __add__(self, other):
        if type(other) == Card:
            self.cards.append(other)
        elif type(other) == Deck:
            self.cards += other.cards

yourDeck = Deck()

boosterPack = Deck(deckType=1)
