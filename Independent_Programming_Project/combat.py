import random

#0 = starter, 1 = common, 2 = uncommon, 3 = rare

class strike():
    rarity = 0 
    type = "atk"
    cost = 1

    def __init__(self, upgrade):
        self.upgrade = upgrade



class defend():
    type = "skill"
    cost = 1

class bash():
    type = "atk"
    cost = 2
    debuff = "vuln"

class neutralize():
    type = "atk"
    cost = 0
    debuff = "weak"

list = [1, 0, 0, 0 , 0]


deck = [strike(False)]

drawPile = deck
discardPile = []
hand = []
game = True

print(deck[0])