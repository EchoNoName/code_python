import random
import math

class acid_slime_small():
    def __init__(self):
        self.name = "Small Acid Slime"
        self.hp = random.randint(8, 13)
    
    def debuff():
        db = ('debuff', 'weak', 1)
        return(db)

    def attack():
        dmg = 3
        return(('attack', dmg))

    def intent(self, turn):
        self.turn = turn
        if self.turn % 2 == 1:
            return acid_slime_small.debuff()
        else:
            return acid_slime_small.attack()
                

class strike():
    rarity = 0 
    type = "attack"
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

class defend():
    rarity = 0 
    type = "skill"
    cost = 1

    def __init__(self, upgrade):
        self.upgrade = upgrade
        if upgrade:
            self.block = 8
            self.name = "Defend+"
        else:
            self.block = 5
            self.name = "Defend"
        self.descr = f"Gain {int(self.block)} block."

def shuffle(draw_pile, discard_pile):
    if draw_pile:
        draw_pile += discard_pile
    else:
        draw_pile = discard_pile
    random.shuffle(draw_pile)
    return(list(draw_pile))

def draw(draw_pile, discard_pile, num):
    cards = []
    while num:
        if draw_pile:
            cards.append(draw_pile[0])
            draw_pile.pop(0)
            num -= 1
        else:
            draw_pile = shuffle(draw_pile, discard_pile)
            discard_pile = []
            if len(draw_pile) == 0:
                num = 0
    return (list(draw_pile), list(discard_pile), list(cards))

enemies = [acid_slime_small(), acid_slime_small()]
combat = True
turn = 1
action = 1
deck = [strike(0), strike(0), strike(0), strike(0), strike(0), defend(0), defend(0), defend(0), defend(0), defend(0)]
draw_pile = deck
random.shuffle(draw_pile)
discard_pile = []
hand = []
player_hp = 70
player_block = 0
player_debuff = []
while combat == True:
    action = 1
    if action == 1:
        for i in enemies:
            print(f"{i.name}, {i.hp}, {i.intent(turn)}")
        hold: list = draw(draw_pile, discard_pile, 5)
        hand = hold[2]
        draw_pile = hold[0]
        discard_pile = hold[1]
        energy = 3
        player_block = 0
        while action:
            for i in hand:
                print(f"{i.name}, ", end="")
            print(" ")
            play = int(input("Enter the index of the card you want to play"))
            if hand[play].type == "attack":
                target = int(input("Enter the index of the target"))
                dmg = hand[play].dmg
                for i in player_debuff:
                    if i[0] == 'weak':
                        dmg = math.floor(dmg * 0.75)
                enemies[target].hp -= dmg
                if enemies[target].hp <= 0:
                    enemies.pop(target)
                energy -= hand[play].cost
                if len(enemies) == 0:
                    break
                for i in enemies:
                    print(f"{i.name}, {i.hp}, {i.intent(turn)}")
            else:
                player_block += hand[play].block
                energy -= hand[play].cost
            discard_pile.append(hand[play])
            hand.pop(play)
            end = input("Do you want to end your turn?")
            if end == 'yes':
                action = 0
                discard_pile += hand
                hand = []
                for i in range(len(player_debuff) - 1, -1, -1):
                    player_debuff[i][1] -= 1
                    if player_debuff[i][1] == 0:
                        player_debuff.pop(i)
        for i in enemies:
            if i.intent(turn)[0] == 'attack':
                player_block -= i.intent(turn)[1]
                if player_block < 0:
                    player_hp += player_block
                    player_block = 0
                print(f"You have {player_hp} hp and {player_block} block left")
            elif i.intent(turn)[0] == 'debuff':
                player_debuff.append([i.intent(turn)[1], i.intent(turn)[2]])
                print(player_debuff)
    turn += 1