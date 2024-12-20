class Card():
    def __init__(self, id, name, rarity, type, cost, card_text, innate, exhaust, retain, ethereal, effect, target):
        self.id = id # Card ID, which is an integer
        self.name = name # Name of the card, a string
        self.rarity = rarity # rarity represented by an integer
        self.type = type # type of card (attack, skill, power, curse, status), represented by an integer
        self.cost = cost # cost of the card, can be just a number, x or a special cost written like ('C', original cost, +/-, condition)
        self.card_text = card_text # Base card text, a string
        self.innate = innate # Boolean representing whether a card is innate
        self.exhaust = exhaust # Boolean representing whether a card is exhaust
        self.retain = retain # Boolean representing whether a card is retain
        self.ethereal = ethereal # Boolean representing whether a card is ethereal
        self.effect = effect # what the card actually does, represented by a dictonary that contains its actions
        self.target = target # The targets of the card, represented by an integer
        self.combat_cost = (None, None) #(Cost, Duration of cost (Played, Turn, Combat))
        self.chaotic = False # whether a card is chaotic, represented by boolean
        


#the card ids will consist of 4 numbers, ABCD, A represents the class of cards, and the rest represents the card number, adding 100 is the upgraded version of the card.
# A = 0, Classless cards, curses, statuses. A = 1, Cursed Swordsman cards

# 0000: (name: rarity:(0 = starter, 1 = common, 2 = uncommon, 3 = rare, 4 = other), type: (0 = atk, 1 = skill, 2 = power, 3 = status, 4 = curse), cost: #, card text: "Card_effect", exhaust, retain, ethereal, effect)
#If mana cost is "U", its unplayable
# Cost: # OR ('C', Original Cost, +/-, Condition) OR 'x'
#Debuffs: 0 = Vulnerable, 1 = Weak, 2 = Negative Strength, 3 = Lose strength at the end of turn, 4 = No Draw, 5 = poison, 6 = lose dex at the end of turn
#Buffs: 0 = strength, 1 = dexterity, 2 = vigour, 3 = blur, 4 = Metalicize, 5 = double tap, 6 = plated armour, 7 = thorns, 8 = regen, 9 = flurry (Play the next card twice), 10 = artifact, 11 = Ritual
#tagets:  Self: 0, target: 1, random: 2, all: 3
#effect:
# dmg: (#, Times, target(Override)
# block: (#, Times)
# buff: (id, stacks, id, stacks, id, stacks...)
# debuff: (id, stacks, id, stacks, id, stacks...)
# draw: #
# discard: #
# place: (start, #, end, position if needed, cost)
# exhaust: (#, location, choice/random/condition/position)
# add: (location, card, #, cost(if applicable))
# search: (location, card/type, #)
# condition (Based on previous effect): (cond, cond eff, norm eff)
# retain: (location, #)
# play: (location, position, discard/exhaust, #)
# Hp: #
# Drawn: (eff)
# turn end: (eff)
# cost: (target, #, cond if applicable)
# modify: (target, eff, modification, combat/Perm)
# power: (name, duration(# OR Perm), amount)
# E: # 
# Exhausted: {eff}
# Discarded: {eff}
# upgrade: (target(s), #, combat/perm)

#Note: When 'exhaust' is put in place for a #, that means # of cards exhausted

card_data = {
    0: ('Curse of the Blade', 4, 4, 'U', 'When drawn, lose 4, At the end of the turn, lose 2 HP. Retain', False, False, True, False, {'drawn': {'Hp': -4}, 'turn end': {'Hp': -2}}, 0),

    1000: ('Slash', 0, 0, 1, 'Deal 6 damage.', False, False, False, False, {'dmg': (6, 1)}, 1),
    1001: ('Bash', 0, 0, 1, 'Deal 8 damage. Apply 2 Vulnerable.', False, False, False, False, {'dmg': (8, 1), 'debuff': (0, 2)}, 1),
    1002: ('Block', 0, 1, 1, 'Gain 5 block.', False, False, False, False, {'block': (5, 1)}, 0),
    1003: ('Inflict Wounds', 0, 0, 0, 'Deal 3 damage. Apply 1 Vulnerable', False, False, False, False, {'dmg': (3, 1), 'debuff': (0, 1)}, 1),
    1004: ("Rampage", 1, 0, 0, 'Deal 6 damage. Add a copy of this card to your discard pile.', False, False, False, False, {'dmg': (6, 1), 'add': ('discard', 1004, 1)}, 1),
    1005: ("Covet", 1, 1, 0, 'Draw 1 card. Discard 1 card, if the card discarded was a Curse, Exhaust it instead.', False, False, False, False, {'draw': 1, 'discard': 1, 'cond': ('curse', {'exhaust': (1, 'discard', 'top')}, {'NA': 0})}, 0),
    1006: ("Flex", 1, 1, 0, 'Gain 2 Temporary Strength.', False, False, False, False, {'buff': (0, 2), 'debuff': (3, 2)}, 0),
    1007: ("War cry", 1, 1, 0, 'Draw 1 card, place 1 card on top of the draw pile, gain 3 Vigour.', False, False, False, False, {'draw': 1, 'place': ('hand', 1, 'deck', 'top')}, 0),
    1008: ("To Basics", 1, 1, 0, 'Add 1 Common card from your draw pile into your hand.', False, False, False, False, {'search': ("deck", 'common', 1)}, 0),
    1009: ("Sword beam", 1, 0, 1, 'Deal 9 damage to all enemies.', False, False, False, False, {'dmg': (9, 1)}, 3),
    1010: ("Grudge", 1, 0, 1, 'Exhaust a card in your hand, deal 9 damage. if the card exhausted was a curse, deal 12 damage to all enemies instead.', False, False, False, False, {'exhuast': (1, 'hand', 'choice'), 'cond': ('curse', {'dmg': (12, 1, 3)}, {'dmg': (9, 1)}) }, 1),
    1011: ("Pummel Strike", 1, 0, 1, 'Deal 9 damage. Draw 1 card.', False, False, False, False, {'dmg': (9, 1), 'draw': 1}, 1),
    1012: ("Twin Slash", 1, 0, 1, 'Deal 5 damage twice.', False, False, False, False, {'dmg': (5, 2)}, 1),
    1013: ("Reckless Charge", 1, 0, 1, 'Deal 11 damage. Add a Curse your draw pile.', False, False, False, False, {'dmg': (11, 1), 'add': ('deck', 'weak curse', 1)}, 1),
    1014: ("Sword Boomerang", 1, 0, 1, 'Deal 3 damage to a random enemy 3 times.', False, False, False, False, {'dmg': (3, 3)}, 2),
    1015: ("Careful Strike", 1, 0, 1, 'Deal 5 damage. Gain 5 block.', False, False, False, False, {'dmg': (5, 1), 'block': (5, 1)}, 1),
    1016: ("Headbutt", 1, 0, 1, 'Deal 9 damage. Place a card from discard pile to top of the draw pile.', False, False, False, False, {'dmg': (9, 1), 'place': ('discard', 1, 'deck', 'top')}, 1),
    1017: ("Shrug it off", 1, 1, 1, 'Gain 8 block. Draw 1 card.', False, False, False, False, {'block': (8, 1), 'draw': 1}, 0),
    1018: ("Grit", 1, 1, 1, 'Gain 5 block. Exhaust a random card in your hand.', False, False, False, False, {'block': (5, 1), 'exhaust': (1, 'hand', 'random')}, 0),
    1019: ("Feint", 1, 1, 1, 'Apply 1 Weak. Gain 5 block.', False, False, False, False, {'debuff': (1, 1), 'block': (5, 1)}, 1),
    1020: ("Preperations", 1, 1, 1, 'Gain 6 block. Choose up to 2 cards to Retain this turn.', False, False, False, False, {'block': (6, 1), 'retain': ('hand', 2)}, 0),
    1021: ("Havoc", 1, 1, 1, 'Play the top card of your draw pile and Exhaust it.', False, False, False, False, {'play': ('deck', 'top', 'exhaust', 1)}, 2),
    1022: ("Crushing blow", 1, 0, 2, 'Deal 12 damage. Apply 2 Weak.', False, False, False, False, {'dmg': (12, 1), 'debuff': (1, 2)}, 1),
    1023: ("Body charge", 1, 0, 1, 'Deal damage equal to your block.', False, False, False, False, {'dmg': ('block', 1)}, 1),
    1024: ("Desperato", 1, 1, 1, 'Gain 6 Vigour, lose 1 Strength.', False, False, False, False, {'buff': (2, 6), 'debuff': (2, 1)}, 0),
    1025: ("Flurry of beams", 2, 0, "X", 'Deal 5 damage to all enemies X times.', False, False, False, False, {'dmg': (5, 'x')}, 3),
    1026: ("Cursed Blade", 2, 0, 1, 'Lose 3 HP. Deal 20 damage. Shuffle a Curse of the Blade into the draw pile.', False, False, False, False, {'Hp': -3, 'dmg': (20, 1), 'add': ('deck', 0, 1)}, 1),
    1027: ("Glooming blade", 2, 0, ('c', 6, '-', 'curse'), 'Deal 20 damage. Cost 1 less Energy for every Curse in the draw pile, discard pile, exhaust pile and hand.', False, False, False, False, {'dmg': (20, 1)}, 1),
    1028: ("Multi-Slash", 2, 0, 1, 'Deal 2 damage 4 times. Exhaust.', False, True, False, False, {'dmg': (2, 4)}, 1),
    1029: ("Aim for the eyes", 2, 0, 2, 'Deal 13 damage. Apply 1 Weak and 1 Vulnerable.', False, False, False, False, {'dmg': (13, 1), 'debuff': (1, 1, 0, 1)}, 1),
    1030: ("Uncontrolled slash", 2, 0, 0, 'Deal 8 damage. Shuffle a Curse into the draw pile.', False, False, False, False, {'dmg': (8, 1), 'add': ('deck', 'weak curse', 1)}, 1),
    1031: ("Consumed", 2, 0, 1, 'Deal 8 damage. This card deals 5 more damage this combat.', False, False, False, False, {'dmg': (8, 1), 'modify': ('self', 'dmg', 5, 'combat')}, 1),
    1032: ("Flaming Strike", 2, 0, 2, 'Deal 12 damage. Can be Upgraded up to 9 times.', False, False, False, False, {'dmg': (12, 1)}, 1),
    1033: ("Purgatory", 2, 0, 3, 'Deal 26 damage to all enemies.', False, False, False, False, {'dmg': (26, 1)}, 3),
    1034: ("Parry", 2, 1, 2, 'Gain 12 block. Whenever you are attacked this turn, apply 2 Vulerable to the attacker.', False, False, False, False, {'block': (12, 1), 'power': ('parry', 1, 2)}, 0),
    1035: ("Deflect", 2, 1, 2, 'Gain 12 block. Whenever you are attacked this turn, deal 4 damage back.', False, False, False, False, {'block': (12, 1), 'power': ('deflect', 1, 4)}, 0),
    1036: ("Sever Soul", 2, 1, 1, 'Exhaust all non-attack cards in hand. For every curse exhausted, gain 1 Strength and draw 1 card.', False, False, False, False, {'exhaust': ('all', 'hand', 'non atk'), 'cond': ('curse', {'buff': (0, 1), 'draw': 1}, {'NA': 0})}, 0),
    1037: ("Cursed Pact", 2, 1, 1, 'Exhaust 1 card in your hand. Draw 2 cards.', False, False, False, False, {'exhaust': (1, 'hand', 'choice'), 'draw': 2}, 0),
    1038: ("Power Through", 2, 1, 0, 'Lose 3 HP. Gain 12 block, shuffle 1 Curse into the draw pile.', False, False, False, False, {'Hp': -3, 'block': (12, 1), 'add': ('deck', 'weak curse', 1)}, 0),
    1039: ("Second wind", 2, 1, 1, 'Exhaust all non-attack cards and gain 5 block for each card exhausted.', False, False, False, False, {'exhaust': ('all', 'hand', 'non atk'), 'cond': ('card', {'block': (5, 1)}, {'NA': 0})}, 0),
    1040: ("Conjour blade", 2, 1, 1, 'Add a random attack card to your hand. It costs 0 this turn.', False, False, False, False, {'add': ('hand', 'atk', 1, 0)}, 0),
    1041: ("Sinister appearance", 2, 1, 0, 'Apply 1 Weak to all enemies. Exhaust.', False, True, False, False, {'debuff': (1, 1)}, 3),
    1042: ("Sentenal", 2, 1, 1, 'Gain 5 block. If this card is exhausted, gain 2 Energy.', False, False, False, False, {'block': (5, 1), 'exhausted': {'E': 2}}, 0),
    1043: ("Bloodletting", 2, 1, 0, 'Lose 3 HP. Gain 2 Energy.', False, False, False, False, {'Hp': -3, 'E': 2}, 0),
    1044: ("Cursed Armour", 2, 1, 1, 'Gain 15 block. Add 2 Curses to your hand.', False, False, False, False, {'block': (15, 1), 'add': ('hand', 'weak curse', 2)}, 0),
    1045: ("Cursed Aura", 2, 1, 2, 'Apply 3 Weak and 3 Vulnerable to all enemies. Exhaust.', False, True, False, False, {'debuff': (1, 3, 0, 3)}, 3),
    1046: ("Disarm", 2, 1, 1, 'Enemy loses 2 Strength. Exhaust.', False, True, False, False, {'debuff': (2, 2)}, 1),
    1047: ("Entrench", 2, 1, 2, 'Double the amount of block you have.', False, False, False, False, {'block': ('2x', 1)}, 0),
    1048: ("Defensive Positioning", 2, 1, 1, 'Gain 2 Blur. ', False, False, False, False, {'buff': (3, 2)}, 0),
    1049: ("Battle Trance", 2, 1, 0, 'Draw 3 cards. You can no longer draw cards this turn. ', False, False, False, False, {'draw': 3, 'debuff': (4, 1)}, 0),
    1050: ("Defensive Stance", 2, 2, 1, 'Gain 3 Metalicize.', False, False, False, False, {'buff': (4, 3)}, 0),
    1051: ("Empower", 2, 2, 1, 'Gain 2 Strength.', False, False, False, False, {'buff': (0, 2)}, 0),
    1052: ("Curse Ward", 2, 2, 2, 'Whenever you draw a Curse, gain 2 block.', False, False, False, False, {'power': ('curse ward', 'perm', 1)}, 0),
    1053: ("Feel no pain", 2, 2, 1, 'Whenever you Exhaust a card, gain 3 block.', False, False, False, False, {'power': ('no pain', 'perm', 3)}, 0),
    1054: ("Evolve", 2, 2, 1, 'Whenever you draw a Status, draw 1 card.', False, False, False, False, {'power': ('evolve', 'perm', 1)}, 0),
    1055: ("Transfer pain", 2, 2, 1, 'Whenever you draw a Curse or Status, deal 6 damage to all enemies.', False, False, False, False, {'power': ('fire breath', 'perm', 6)}, 0),
    1056: ("Dark Embrace", 2, 2, 2, 'Whenever a card is exhausted, draw 1 card.', False, False, False, False, {'power': ('embrace', 'perm', 1)}),
    1057: ("Devouring Blade", 3, 0, 2, 'Deal 12 damage. If Fatal, increase this cards damage by 3 permanently. Exhaust.', False, True, False, False, {'dmg': (12, 1), 'cond': ('lethal', {'modify': ('self', 'dmg', 3, 'perm')}, {'NA': 0})}, 1),
    1058: ("Void Strike", 3, 0, 0, 'Deal 3 damage. Apply 2 Vulnerable. 2 Weak and 2 Poison. Exhaust.', False, True, False, False, {'dmg': (3, 1), 'debuff': (0, 2, 1, 2, 5, 2)}, 1),
    1059: ("Cursed flames", 3, 0, 2, 'Deal 21 to all enemies. Shuffle 2 Curses into the discard pile.', False, False, False, False, {'dmg': (21, 1), 'add': ('discard', 'weak curse', 2)}, 3),
    1060: ("Bloodlust", 3, 0, 2, 'Deal 4 damage to all enemies. Heal HP equal to the unblocked damage dealt.', False, False, False, False, {'dmg': (4, 1), 'Hp': 'dmg'}, 3),
    1061: ("Black Wind", 3, 0, 0, 'Deal 10 damage for each Curse in your hand. Retain.', False, False, True, False, {'dmg': (10, 'curse')}, 1),
    1062: ("Black flame", 3, 0, 2, 'Exhaust your hand. Deal 7 damage for each card exhausted. ', False, False, False, False, {'exhaust': ('all', 'hand', 'all'), 'cond': ('card', {'dmg': (7, 1)}, {'NA': 0})}, 1),
    1063: ("Generational Skill", 3, 1, 1, 'Exhaust all cards in your hand, shuffle a Curse into the draw pile and draw 2 for each card exhausted. gain 1 Energy. Exhaust', False, True, False, False, {'exhaust': ('all', 'hand', 'all'), 'cond': ('card', {'add': ('deck', 'weak curse', 1), 'draw': 2}, {'NA': 0}), 'E': 1}, 0),
    1064: ("Fey's Offering", 3, 1, 0, 'Lose 6 HP. Draw 3 cards. Gain 2 Energy. Exhaust.', False, True, False, False, {'Hp': -6, 'draw': 3, 'E': 2}, 0),
    1065: ("Mirror image", 3, 1, 1, 'Your next attack is played twice.', False, False, False, False, {'buff': (5, 1)}, 0),
    1066: ("Hallucinations", 3, 1, 1, 'Add 1 card from your exhaust pile to your hand. Exhaust.', False, True, False, False, {'place': ('exhaust', 1, 'hand')}, 0),
    1067: ("Final Gambit", 3, 1, "X", 'Exhaust EVERYTHING. Add X + 1 cards from your exhaust pile to your hand, they cost 0 this turn. At the end of your turn, Exhaust EVERYTHING. Exhaust', False, True, False, False, {'exhaust': ('all', 'all'), 'place': ('exhaust', 'x + 1', 'hand', 'NA', 0), 'power': ('final gambit', 1, 1)}, 0),
    1068: ("Impervious", 3, 1, 2, 'Gain 30 block. Exhaust', False, True, False, False, {'block': (30, 1)}, 0),
    1069: ("Corruption Form", 3, 2, 3, 'At the start of your turn, lose 1 HP and gain 3 Strength.', False, False, False, False, {'power': ('form1', 'perm', 1)}, 0),
    1070: ("Phantom blades", 3, 2, 2, 'At the start of your turn, gain 4 Vigour.', False, False, False, False, {'power': ('blades', 'perm', 4)}, 0),
    1071: ("Seeing red", 3, 2, 1, 'Draw 2 cards at the start of turn and add a Curse to hand.', False, False, False, False, {'power': ('seeing red', 'perm', 1)}, 0),
    1072: ("Clear mind", 3, 2, 3, 'At the start of turn, you can exhaust a card from your hand to gain 8 block.', False, False, False, False, {'power': ('adapt', 'perm', 1)}, 0),
    1073: ("Corruption", 3, 2, 2, 'Curses no longer have negative effects.', False, False, False, False, {'power': ('pure', 'perm', 1)}, 0),
    1074: ("Eternal flames", 3, 2, 0, 'Gain 3 Energy, Draw 3 cards. If you end your turn with no Energy, lose 4 HP.', False, False, False, False, {'E': 3, 'draw': 3, 'power': ('eternal', 'perm', 4)}, 0),
    #below are upgrades
    1100: ('Slash+', 0, 0, 1, 'Deal 9 damage.', False, False, False, False, {'dmg': (9, 1)}, 1),
    1101: ('Bash+', 0, 0, 1, 'Deal 12 damage. Apply 3 Vulnerable.', False, False, False, False, {'dmg': (12, 1), 'debuff': (0, 3)}, 1),
    1102: ('Block+', 0, 1, 1, 'Gain 8 block.', False, False, False, False, {'block': (8, 1)}, 0),
    1103: ('Inflict Wounds+', 0, 0, 0, 'Deal 4 damage. Apply 2 Vulnerable', False, False, False, False, {'dmg': (4, 1), 'debuff': (0, 2)}, 1),
    1104: ("Rampage+", 1, 0, 0, 'Deal 8 damage. Add a copy of this card to your discard pile.', False, False, False, False, {'dmg': (8, 1), 'add': ('discard', 1104, 1)}, 1),
    1105: ("Covet+", 1, 1, 0, 'Draw 2 card. Discard 2 card, if the card discarded was a Curse, Exhaust it instead.', False, False, False, False, {'draw': 2, 'discard': 2, 'cond': ('curse', {'exhaust': (1, 'discard', 'top')}, {'NA': 0})}, 0),
    1106: ("Flex+", 1, 1, 0, 'Gain 4 Temporary Strength.', False, False, False, False, {'buff': (0, 4), 'debuff': (3, 4)}, 0),
    1107: ("War cry+", 1, 1, 0, 'Draw 2 card, place 1 card on top of the draw pile, gain 3 Vigour.', False, False, False, False, {'draw': 2, 'place': ('hand', 1, 'deck', 'top')}, 0),
    1108: ("To Basics+", 1, 1, 0, 'Add 2 Common card from your draw pile into your hand.', False, False, False, False, {'search': ("deck", 'common', 2)}, 0),
    1109: ("Sword beam+", 1, 0, 1, 'Deal 11 damage to all enemies.', False, False, False, False, {'dmg': (11, 1)}, 3),
    1110: ("Grudge+", 1, 0, 1, 'Exhaust a card in your hand, deal 11 damage. if the card exhausted was a curse, deal 15 damage to all enemies instead.', False, False, False, False, {'exhuast': (1, 'hand', 'choice'), 'cond': ('curse', {'dmg': (15, 1, 3)}, {'dmg': (11, 1)}) }, 1),
    1111: ("Pummel Strike+", 1, 0, 1, 'Deal 12 damage. Draw 2 card.', False, False, False, False, {'dmg': (12, 1), 'draw': 2}, 1),
    1112: ("Twin Slash+", 1, 0, 1, 'Deal 7 damage twice.', False, False, False, False, {'dmg': (7, 2)}, 1),
    1113: ("Reckless Charge+", 1, 0, 1, 'Deal 15 damage. Add a Curse your draw pile.', False, False, False, False, {'dmg': (15, 1), 'add': ('deck', 'weak curse', 1)}, 1),
    1114: ("Sword Boomerang+", 1, 0, 1, 'Deal 3 damage to a random enemy 4 times.', False, False, False, False, {'dmg': (3, 4)}, 2),
    1115: ("Careful Strike+", 1, 0, 1, 'Deal 7 damage. Gain 7 block.', False, False, False, False, {'dmg': (7, 1), 'block': (7, 1)}, 1),
    1116: ("Headbutt+", 1, 0, 1, 'Deal 11 damage. Place a card from discard pile to top of the draw pile.', False, False, False, False, {'dmg': (11, 1), 'place': ('discard', 1, 'deck', 'top')}, 1),
    1117: ("Shrug it off+", 1, 1, 1, 'Gain 11 block. Draw 1 card.', False, False, False, False, {'block': (11, 1), 'draw': 1}, 0),
    1118: ("Grit+", 1, 1, 1, 'Gain 8 block. Exhaust a card in your hand.', False, False, False, False, {'block': (8, 1), 'exhaust': (1, 'hand', 'choice')}, 0),
    1119: ("Feint+", 1, 1, 1, 'Apply 1 Weak. Gain 7 block.', False, False, False, False, {'debuff': (1, 1), 'block': (7, 1)}, 1),
    1120: ("Preperations+", 1, 1, 1, 'Gain 8 block. Choose up to 3 cards to Retain this turn.', False, False, False, False, {'block': (8, 1), 'retain': ('hand', 3)}, 0),
    1121: ("Havoc+", 1, 1, 1, 'Play the top 2 cards of your draw pile and Exhaust it.', False, False, False, False, {'play': ('deck', 'top', 'exhaust', 2)}, 2),
    1122: ("Crushing blow+", 1, 0, 2, 'Deal 14 damage. Apply 3 Weak.', False, False, False, False, {'dmg': (14, 1), 'debuff': (1, 3)}, 1),
    1123: ("Body charge+", 1, 0, 0, 'Deal damage equal to your block.', False, False, False, False, {'dmg': ('block', 1)}, 1),
    1124: ("Desperato+", 1, 1, 0, 'Gain 6 Vigour, lose 1 Strength.', False, False, False, False, {'buff': (2, 6), 'debuff': (2, 1)}, 0),
    1125: ("Flurry of beams+", 2, 0, "X", 'Deal 8 damage to all enemies X times.', False, False, False, False, {'dmg': (8, 'x')}, 3),
    1126: ("Cursed Blade+", 2, 0, 1, 'Lose 2 HP. Deal 26 damage. Shuffle a Curse of the Blade into the draw pile.', False, False, False, False, {'Hp': -2, 'dmg': (26, 1), 'add': ('deck', 0, 1)}, 1),
    1127: ("Glooming blade+", 2, 0, ('c', 5, '-', 'curse'), 'Deal 26 damage. Cost 1 less Energy for every Curse in the draw pile, discard pile, exhaust pile and hand.', False, False, False, False, {'dmg': (26, 1)}, 1),
    1128: ("Multi-Slash+", 2, 0, 1, 'Deal 2 damage 5 times. Exhaust.', False, True, False, False, {'dmg': (2, 5)}, 1),
    1129: ("Aim for the eyes+", 2, 0, 2, 'Deal 13 damage. Apply 2 Weak and 2 Vulnerable.', False, False, False, False, {'dmg': (13, 1), 'debuff': (1, 2, 0, 2)}, 1),
    1130: ("Uncontrolled slash+", 2, 0, 0, 'Deal 11 damage. Shuffle a Curse into the draw pile.', False, False, False, False, {'dmg': (11, 1), 'add': ('deck', 'weak curse', 1)}, 1),
    1131: ("Consumed+", 2, 0, 1, 'Deal 8 damage. This card deals 8 more damage this combat.', False, False, False, False, {'dmg': (8, 1), 'modify': ('self', 'dmg', 8, 'combat')}, 1),
    1132: ("Flaming Strike+", 2, 0, 2, 'Deal 16 damage. Can be Upgraded up to 8 times.', False, False, False, False, {'dmg': (16, 1)}, 1),
    1133: ("Purgatory+", 2, 0, 3, 'Deal 30 damage to all enemies.', False, False, False, False, {'dmg': (30, 1)}, 3),
    1134: ("Parry+", 2, 1, 2, 'Gain 16 block. Whenever you are attacked this turn, apply 2 Vulerable to the attacker.', False, False, False, False, {'block': (16, 1), 'power': ('parry', 1, 2)}, 0),
    1135: ("Deflect+", 2, 1, 2, 'Gain 16 block. Whenever you are attacked this turn, deal 5 damage back.', False, False, False, False, {'block': (16, 1), 'power': ('deflect', 1, 5)}, 0),
    1136: ("Sever Soul+", 2, 1, 1, 'Exhaust all Ailments in hand. For every curse exhausted, gain 1 Strength and draw 1 card.', False, False, False, False, {'exhaust': ('all', 'hand', 'ailment'), 'cond': ('curse', {'buff': (0, 1), 'draw': 1}, {'NA': 0})}, 0),
    1137: ("Cursed Pact+", 2, 1, 1, 'Exhaust 1 card in your hand. Draw 3 cards.', False, False, False, False, {'exhaust': (1, 'hand', 'choice'), 'draw': 3}, 0),
    1138: ("Power Through+", 2, 1, 0, 'Lose 3 HP. Gain 15 block, Add 1 Curse into the hand.', False, False, False, False, {'Hp': -3, 'block': (15, 1), 'add': ('hand', 'weak curse', 1)}, 0),
    1139: ("Second wind+", 2, 1, 1, 'Exhaust all non-attack cards and gain 7 block for each card exhausted.', False, False, False, False, {'exhaust': ('all', 'hand', 'non atk'), 'cond': ('card', {'block': (7, 1)}, {'NA': 0})}, 0),
    1140: ("Conjour blade+", 2, 1, 0, 'Add a random attack card to your hand. It costs 0 this turn.', False, False, False, False, {'add': ('hand', 'atk', 1, 0)}, 0),
    1141: ("Sinister appearance+", 2, 1, 0, 'Apply 2 Weak to all enemies. Exhaust.', False, True, False, False, {'debuff': (1, 2)}, 3),
    1142: ("Sentenal+", 2, 1, 1, 'Gain 8 block. If this card is exhausted, gain 3 Energy.', False, False, False, False, {'block': (8, 1), 'exhausted': {'E': 3}}, 0),
    1143: ("Bloodletting+", 2, 1, 0, 'Lose 3 HP. Gain 3 Energy.', False, False, False, False, {'Hp': -3, 'E': 3}, 0),
    1144: ("Cursed Armour+", 2, 1, 1, 'Gain 20 block. Add 2 Curses to your hand.', False, False, False, False, {'block': (20, 1), 'add': ('hand', 'weak curse', 2)}, 0),
    1145: ("Cursed Aura+", 2, 1, 2, 'Apply 5 Weak and 5 Vulnerable to all enemies. Exhaust.', False, True, False, False, {'debuff': (1, 5, 0, 5)}, 3),
    1146: ("Disarm+", 2, 1, 1, 'Enemy loses 3 Strength. Exhaust.', False, True, False, False, {'debuff': (2, 3)}, 1),
    1147: ("Entrench+", 2, 1, 1, 'Double the amount of block you have.', False, False, False, False, {'block': ('2x', 1)}, 0),
    1148: ("Defensive Positioning+", 2, 1, 0, 'Gain 2 Blur. ', False, False, False, False, {'buff': (3, 2)}, 0),
    1149: ("Battle Trance+", 2, 1, 0, 'Draw 4 cards. You can no longer draw cards this turn. ', False, False, False, False, {'draw': 4, 'debuff': (4, 1)}, 0),
    1150: ("Defensive Stance+", 2, 2, 1, 'Gain 4 Metalicize.', False, False, False, False, {'buff': (4, 4)}, 0),
    1151: ("Empower+", 2, 2, 1, 'Gain 3 Strength.', False, False, False, False, {'buff': (0, 3)}, 0),
    1152: ("Curse Ward+", 2, 2, 2, 'Whenever you draw a Curse, gain 2 block and draw 1 card.', False, False, False, False, {'power': ('curse ward+', 'perm', 1)}, 0),
    1153: ("Feel no pain+", 2, 2, 1, 'Whenever you Exhaust a card, gain 4 block.', False, False, False, False, {'power': ('no pain', 'perm', 4)}, 0),
    1154: ("Evolve+", 2, 2, 1, 'Whenever you draw an Ailment, draw 1 card.', False, False, False, False, {'power': ('evolve+', 'perm', 1)}, 0),
    1155: ("Transfer pain+", 2, 2, 1, 'Whenever you draw a Curse or Status, deal 8 damage to all enemies.', False, False, False, False, {'power': ('fire breath', 'perm', 8)}, 0),
    1156: ("Dark Embrace+", 2, 2, 1, 'Whenever a card is exhausted, draw 1 card.', False, False, False, False, {'power': ('embrace', 'perm', 1)}),
    1157: ("Devouring Blade+", 3, 0, 2, 'Deal 14 damage. If Fatal, increase this cards damage by 4 permanently. Exhaust.', False, True, False, False, {'dmg': (14, 1), 'cond': ('lethal', {'modify': ('self', 'dmg', 4, 'perm')}, {'NA': 0})}, 1),
    1158: ("Void Strike+", 3, 0, 0, 'Deal 4 damage. Apply 4 Vulnerable. 4 Weak and 4 Poison. Exhaust.', False, True, False, False, {'dmg': (4, 1), 'debuff': (0, 4, 1, 4, 5, 4)}, 1),
    1159: ("Cursed flames+", 3, 0, 2, 'Deal 28 to all enemies. Shuffle 2 Curses into the discard pile.', False, False, False, False, {'dmg': (28, 1), 'add': ('discard', 'weak curse', 2)}, 3),
    1160: ("Bloodlust+", 3, 0, 2, 'Deal 5 damage to all enemies. Heal HP equal to the unblocked damage dealt.', False, False, False, False, {'dmg': (5, 1), 'Hp': 'dmg'}, 3),
    1161: ("Black Wind+", 3, 0, 0, 'Deal 12 damage for each Curse in your hand. Retain.', False, False, True, False, {'dmg': (12, 'curse')}, 1),
    1162: ("Black flame+", 3, 0, 2, 'Exhaust your hand. Deal 10 damage for each card exhausted. ', False, False, False, False, {'exhaust': ('all', 'hand', 'all'), 'cond': ('card', {'dmg': (10, 1)}, {'NA': 0})}, 1),
    1163: ("Generational Skill+", 3, 1, 0, 'Exhaust all cards in your hand, shuffle a Curse into the draw pile and draw 2 for each card exhausted. gain 1 Energy. Exhaust', False, True, False, False, {'exhaust': ('all', 'hand', 'all'), 'cond': ('card', {'add': ('deck', 'weak curse', 1), 'draw': 2}, {'NA': 0}), 'E': 1}, 0),
    1164: ("Fey's Offering+", 3, 1, 0, 'Lose 6 HP. Draw 5 cards. Gain 2 Energy. Exhaust.', False, True, False, False, {'Hp': -6, 'draw': 5, 'E': 2}, 0),
    1165: ("Mirror image+", 3, 1, 1, 'Your next 2 attacks are played twice.', False, False, False, False, {'buff': (5, 2)}, 0),
    1166: ("Hallucinations+", 3, 1, 0, 'Add 1 card from your exhaust pile to your hand. Exhaust.', False, True, False, False, {'place': ('exhaust', 1, 'hand')}, 0),
    1167: ("Final Gambit+", 3, 1, "X", 'Exhaust EVERYTHING. Add X + 2 cards from your exhaust pile to your hand, they cost 0 this turn. At the end of your turn, Exhaust EVERYTHING. Exhaust', False, True, False, False, {'exhaust': ('all', 'all'), 'place': ('exhaust', 'x + 2', 'hand', 'NA', 0), 'power': ('final gambit', 1, 1)}, 0),
    1168: ("Impervious+", 3, 1, 2, 'Gain 40 block. Exhaust', False, True, False, False, {'block': (40, 1)}, 0),
    1169: ("Corruption Form+", 3, 2, 3, 'At the start of your turn, lose 1 HP and gain 4 Strength.', False, False, False, False, {'power': ('form1+', 'perm', 1)}, 0),
    1170: ("Phantom blades+", 3, 2, 1, 'At the start of your turn, gain 4 Vigour.', False, False, False, False, {'power': ('blades', 'perm', 4)}, 0),
    1171: ("Seeing red+", 3, 2, 1, 'Draw 2 cards at the start of turn and add a Curse to hand.', True, False, False, False, {'power': ('seeing red', 'perm', 1)}, 0),
    1172: ("Clear mind+", 3, 2, 2, 'At the start of turn, you can exhaust a card from your hand to gain 8 block.', False, False, False, False, {'power': ('adapt', 'perm', 1)}, 0),
    1173: ("Corruption+", 3, 2, 2, 'Curses no longer have negative effects.', True, False, False, False, {'power': ('pure', 'perm', 1)}, 0),
    1174: ("Eternal flames+", 3, 2, 0, 'Gain 3 Energy, Draw 4 cards. If you end your turn with no Energy, lose 3 HP.', False, False, False, False, {'E': 3, 'draw': 4, 'power': ('eternal', 'perm', 3)}, 0),

    1232: ("Flaming Strike+2", 2, 0, 2, 'Deal 21 damage. Can be Upgraded up to 7 more times.', False, False, False, False, {'dmg': (21, 1)}, 1),
    1332: ("Flaming Strike+3", 2, 0, 2, 'Deal 27 damage. Can be Upgraded up to 6 more times.', False, False, False, False, {'dmg': (27, 1)}, 1),
    1432: ("Flaming Strike+4", 2, 0, 2, 'Deal 34 damage. Can be Upgraded up to 5 more time.', False, False, False, False, {'dmg': (34, 1)}, 1),
    1532: ("Flaming Strike+5", 2, 0, 2, 'Deal 42 damage. Can be Upgraded up to 4 more time.', False, False, False, False, {'dmg': (42, 1)}, 1),
    1632: ("Flaming Strike+5", 2, 0, 2, 'Deal 51 damage. Can be Upgraded up to 3 more time.', False, False, False, False, {'dmg': (51, 1)}, 1),
    1732: ("Flaming Strike+5", 2, 0, 2, 'Deal 61 damage. Can be Upgraded up to 2 more time.', False, False, False, False, {'dmg': (61, 1)}, 1),
    1832: ("Flaming Strike+5", 2, 0, 2, 'Deal 72 damage. Can be Upgraded up to 1 more time.', False, False, False, False, {'dmg': (72, 1)}, 1),
    1932: ("Flaming Strike+5", 2, 0, 2, 'Deal 84 damage.', False, False, False, False, {'dmg': (84, 1)}, 1),
}