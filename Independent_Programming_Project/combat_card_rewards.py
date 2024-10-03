import random

cardSelect = []

cardPoolCommon = ["Strike", "Defend", "Bash"] #Pool of cards
cardPoolUncomm = ["Flame Barrier", "Uppercut", "Battle Trace"]
cardPoolRare = ["Demon Form", "Corruption", "Offering"]

combat = "normal"

rareChanceOff = -5
baseRareChance = 0

if combat == "normal":
    baseRareChance = 3
    uncommChance = 37
elif combat == "elite":
    baseRareChance = 10
    uncommChance = 40
else:
    baseRareChance = 105

for i in range(3):
    x = random.randrange(0, 100)
    rareChance = baseRareChance + rareChanceOff
    if x < rareChance or combat == "boss":
        cardPoolSel = [item for item in cardPoolRare if item not in cardSelect]
        cardSelect.append(random.choice(cardPoolSel))
        if combat != "boss":
            rareChanceOff = -5
    elif x < uncommChance:
        cardPoolSel = [item for item in cardPoolUncomm if item not in cardSelect]
        cardSelect.append(random.choice(cardPoolSel))
    else: 
        cardPoolSel = [item for item in cardPoolCommon if item not in cardSelect]
        cardSelect.append(random.choice(cardPoolSel))
        rareChanceOff += 1

deck = []

print(cardSelect)

i = int(input("Pick a card:"))

deck.append(cardSelect[i])

print(deck[0])



