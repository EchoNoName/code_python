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
# gamble: # (Do a mulligan # of times)
# potion: (Slots, Type), adds potions to empty slots
# MaxHp: #
# Chaotic: Location

# 'NAME': ('DESCRIPTION', 'TIME OF USE', ('EFFECT': 'MAGNITUDE'...), 'TARGET')

potions = {
    "Attack Potion": ("Add 1 of 3 random Attack cards to your hand, it costs 0 this turn.", 'combat', {'add': ('hand', 'trial atk', 1, 0)}, 0),
    "Skill Potion": ("Add 1 of 3 random Skill cards to your hand, it costs 0 this turn.", 'combat', {'add': ('hand', 'trial skill', 1, 0)}, 0),
    "Power Potion": ("Add 1 of 3 random Power cards to your hand, it costs 0 this turn.", 'combat', {'add': ('hand', 'trial power', 1, 0)}, 0),
    "Utilities Potion": ("Add 1 of 3 random Non-class cards to your hand, it costs 0 this turn.", 'combat', {'add': ('hand', 'trial atk', 1, 0)}, 0),
    "Blessing of the Forge": ("Upgrade all cards in your hand for the rest of combat.", 'combat', {'upgrade': ('hand', 'all', 'combat')}, 0),
    "Block Potion": ("Gain 12 block.", 'combat', {'block': (12, 1)}, 0),
    "Strength Potion": ("Gain 2 Strength.", 'combat', {'buff': (0, 2)}, 0),
    "Dexterity Potion": ("Gain 2 Dexterity.", 'combat', {'buff': (1, 2)}, 0),
    "Flex Potion": ("Gain 5 Temporary Strength.", 'combat', {'buff': (0, 5), 'debuff': (3, 5)}, 0),
    "Speed Potion": ("Gain 5 Temporary Dexterity.", 'combat', {'buff': (1, 5), 'debuff': (6, 5)}, 0),
    "Fire Potion": ("Deal 20 Damage.", 'combat', {'dmg': (20, 1)}, 0),
    "Explosive Potion": ("Deal 10 Damage to all enemies.", 'combat', {'dmg': (10, 1)}, 0),
    "Fear Potion": ("Apply 3 Vulnerable to an enemy.", 'combat', {'debuff': (0, 3)}, 1),
    "Weak Potion": ("Apply 3 Weak to an enemy.", 'combat', {'debuff': (1, 3)}, 1),
    "Energy Potion": ("Gain 2 Energy.", 'combat', {'E': 2}),
    "Swift Potion": ("Draw 3 cards.", 'combat', {'draw': 3}),
    "Ancient Potion": ("Gain 1 Artifact.", 'combat', {'buff': (10, 1)}, 0),
    "Thorns Potion": ("Gain 3 Thorns.", 'combat', {'buff': (7, 3)}, 0),
    "Liquid Metal": ("Gain 4 Plated Armour.", 'combat', {'buff': (6, 4)}, 0),
    "Regen Potion": ("Gain 5 Regeneration.", 'combat', {'buff': (8, 5)}, 0),
    "Memory Potion": ("Choose 1 card from the discard pile and add it to the hand, it costs 0 this turn.", 'combat', {'place': ('discard', 1, 'hand', None, 0)}, 0),
    "Duplicate Potion": ("Your next card is played twice.", 'combat', {'buff': (9, 1)}, 0),
    "Gambler's Potion": ("Discard any number of cards, then draw that many.", 'combat', {'gamble': 1}),
    "Chaos Potion": ("Play the top 3 cards of your Draw pile (This doesn't spend Energy).", 'combat', {'play': ('deck', 'top', 3)}, 2),
    "Ritual Potion": ("Gain 1 Ritual.", 'combat', {'buff': (11, 1)}, 0),
    "Entropic Brew": ("Fill all your empty potion slots with random potions.", 'all', {'potion': ('all', 'random')}, 0),
    "Fairy in a Bottle": ("When you would die, heal to 30% of your Max HP instead and discard this potion.", 'passive', {'Hp': '30'}, 0),
    "Fruit Juice": ("Gain 5 Max HP.", 'all', {'MaxHp': 5}, 0),
    "Smoke Bomb": ("Escape from a non-boss combat. Receive no rewards.", 'combat', {'escape': 'non boss'}, 0),
    "Chaotic Potion": ("Draw 5 cards. Randomize the costs of all cards in your hand for the rest of the combat.", 'combat', {'draw': 5, 'chaotic': 'hand'}),
    "Blood Potion": ("Heal for 20% of your Max Hp", 'all', {'Hp': '20'}),
    "Holy Water": ("Exhaust any number of cards in your hand.", {'exhaust': ('any', 'hand', 'choice')}, 0)
}
