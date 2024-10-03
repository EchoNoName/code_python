class strike():
    rarity = 0 
    type = "atk"
    cost = 1

    def __init__(self, upgrade):
        self.upgrade = upgrade
        if upgrade:
            self.dmg = 9
            self.name = "Strike+"
        else:
            self.dmg = 6
            self.name = "Strike"

#adding cards
deck = [strike(True)]
deck.append(strike(False))
print(deck[1].dmg)
print(deck)