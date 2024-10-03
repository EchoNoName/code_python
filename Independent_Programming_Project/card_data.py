class strike():
    rarity = 0 
    type = "atk"
    cost = 1

    def __init__(self, upgrade):
        self.upgrade = upgrade
        if upgrade:
            self.dmg = 9
        else:
            self.dmg = 6

card = strike(True)
print(card.dmg)