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

potions = {
    "Attack Potion": ("Add 1 of 3 random Attack cards to your hand, it costs 0 this turn.", {'add': ('hand', 'trial atk', 1, 0)}, 0),
    "Skill Potion": ("Add 1 of 3 random Skill cards to your hand, it costs 0 this turn.", {'add': ('hand', 'trial skill', 1, 0)}, 0),
    "Power Potion": ("Add 1 of 3 random Power cards to your hand, it costs 0 this turn.", {'add': ('hand', 'trial power', 1, 0)}, 0),
    "Utilities Potion": ("Add 1 of 3 random Non-class cards to your hand, it costs 0 this turn.", {'add': ('hand', 'trial atk', 1, 0)}, 0),
    "Blessing of the Forge": ("Upgrade all cards in your hand for the rest of combat.", {'upgrade': ('hand', 'all', 'combat')}, 0),
    "Block Potion": ("Gain 12 block.", {'block': (12, 1)}, 0),
    "Strength Potion": ("Gain 2 Strength.", {'buff': (0, 2)}, 0),
    "Dexterity Potion": ("Gain 2 Dexterity.", {'buff': (1, 2)}, 0),
    "Flex Potion": ("Gain 5 Temporary Strength.", {'buff': (0, 5), 'debuff': (3, 5)}, 0),
    "Speed Potion": ("Gain 5 Temporary Dexterity.", {'buff': (1, 5), 'debuff': (6, 5)}, 0),
    "Fire Potion": ("Deal 20 Damage.", {'dmg': (20, 1)}, 0),
    "Explosive Potion": ("Deal 10 Damage to all enemies.", {'dmg': (10, 1)}, 0),
    "Fear Potion": ("Apply 3 Vulnerable to an enemy."),
    "Weak Potion": ("Apply 3 Weak to an enemy."),
    "Energy Potion": ("Gain 2 Energy."),
    "Swift Potion": ("Draw 3 cards."),
    "Ancient Potion": ("Gain 1 Artifact."),
    "Thorns Potion": ("Gain 3 Thorns."),
    "Liquid Metal": ("Gain 4 Plated Armour."),
    "Regen Potion": ("Gain 5 Regeneration."),
    "Memory Potion": ("Choose 1 card from the discard pile and add it to the hand, it costs 0 this turn."),
    "Duplicate Potion": ("Your next card is played twice."),
    "Gambler's Potion": ("Discard any number of cards, then draw that many."),
    "Chaos Potion": ("Play the top 3 cards of your Draw pile (This doesn't spend Energy)."),
    "Ritual Potion": ("Gain 1 Ritual."),
    "Entropic Brew": ("Fill all your empty potion slots with random potions."),
    "Fairy in a Bottle": ("When you would die, heal to 30% of your Max HP instead and discard this potion."),
    "Fruit Juice": ("Gain 5 Max HP."),
    "Smoke Bomb": ("Escape from a non-boss combat. Receive no rewards."),
    "Chaotic Potion": ("Draw 5 cards. Randomize the costs of all cards in your hand for the rest of the combat."),
    "Blood Potion": ("Heal for 20% of your Max Hp"),
    "Holy Water": ("Exhaust any number of cards in your hand.")
}
