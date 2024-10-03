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

deck = [strike(0), strike(1), strike(0), strike(0)]

upgrade_list = []

for i in deck:
    if i.upgrade == False:
        upgrade_list.append(i)

print(upgrade_list)
input = int(input("Choose card to upgrade (not the index)"))

for i in deck:
    if i.upgrade == False:
        input -= 1
        if input == 0:
            setattr(i, 'upgrade', i.upgrade + 1) 
