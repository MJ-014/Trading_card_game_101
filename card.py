from random import randint

class Card:
    def __init__(self, cardType=""):
        self.cardType = cardType
    
    def chooseTypeRandomly(self):
        types = ["Fighter", "Healer", "Trainer", "Rare"]
        numb = randint(0, 101)

        if numb in range(0, 51):
            self.cardType = types[0]
        elif numb in range(51, 76):
            self.cardType = types[2]
        elif numb in range(76, 100):
            self.cardType = types[1]
        elif numb == 100:
            self.cardType = types[3]
        else:
            self.cardType = "No"


