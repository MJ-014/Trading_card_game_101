from random import randint

class Card:
    def __init__(self, cardType):
        self.type = cardType

    def chooseTypeRandomly(self):
        types = ["Fighter", "Healer", "Trainer", "Rare", "Energy"]
        numb = randint(0, 101)
        if numb == 17:
            return types[3]
        elif numb % 10 == 0:
            return types[0]
