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
        self.descr = f"Deal {int(self.dmg)} damage."

class searing():
    rarity = 2 
    type = "atk"
    cost = 2

    def __init__(self, upgrade):
        self.upgrade = upgrade
        self.dmg = int(upgrade) * (int(upgrade) + 7) / 2 + 12
        if int(upgrade) == 0:
            self.name = "Searing Blow"
        elif int(upgrade) == 1:
            self.name = "Searing Blow+"
        else:
            self.name = f"searing Blow+{upgrade}"
        self.descr = f"Deal {int(self.dmg)} damage. Can be upgraded any numbers of times."

#adding cards
deck = [searing(3)]
deck.append(strike(False))
print(deck[0].dmg)
print(deck[0].descr)