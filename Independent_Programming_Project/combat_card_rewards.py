import random

cardSelect = [] #List of cards the player selects from to add to the deck

cardPoolCommon = ["Strike", "Defend", "Bash"] #Pool of cards based on rarity
cardPoolUncomm = ["Flame Barrier", "Uppercut", "Battle Trace"]
cardPoolRare = ["Demon Form", "Corruption", "Offering"]

combat = "normal" #combat reward type

rareChanceOff = -5 #Rare chance offset
baseRareChance = 0 #Initializing variable for base rare chance

if combat == "normal": #base rare chance decided by combat type
    baseRareChance = 3
    uncommChance = 37
elif combat == "elite":
    baseRareChance = 10
    uncommChance = 40
else:
    baseRareChance = 105 #guarenteed rare for boss fights

card_choice_num = 3 #can be changed dependant on other modifiers

for i in range(card_choice_num): #Runs x amount of random card choices
    x = random.randrange(0, 100) #random num from 0-99 inclusive
    rareChance = baseRareChance + rareChanceOff #calculate actual rare chance
    if x < rareChance or combat == "boss": #if the random num rolled is below rare chance that means they got a rare card, or if its a boss fight
        cardPoolSel = [item for item in cardPoolRare if item not in cardSelect] #create a pool of cards from the correct rarity and remove dupes from cards already part of the selection
        cardSelect.append(random.choice(cardPoolSel)) #random card chosen from the pool
        if combat != "boss":
            rareChanceOff = -5 #if its not a boss card reward, reset the rare chance offset
    elif x < uncommChance: #same as above expect for uncommons
        cardPoolSel = [item for item in cardPoolUncomm if item not in cardSelect]
        cardSelect.append(random.choice(cardPoolSel))
    else:  #for commons
        cardPoolSel = [item for item in cardPoolCommon if item not in cardSelect]
        cardSelect.append(random.choice(cardPoolSel))
        rareChanceOff += 1 #increase the rare chance offset when ever a common card is rolled

deck = [] #player's deck

print(cardSelect) #prints out the cards avalible to select

i = int(input("Pick a card:")) #takes user choice

deck.append(cardSelect[i]) # add chosen card to deck

print(deck[0])



