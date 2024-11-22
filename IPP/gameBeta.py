import effects
class Relics: # Relic Object Class
    def __init__(self, name, effect, condition, consumable, magnitude = 1):
        self.name = name # Name
        self.effect = effect # Effect represented by a function
        self.condition = condition # Condition for the effect
        self.consumable = consumable # If the relic is one time use
        self.used = None
        if consumable == True:
            self.used = False
        self.magnitude = magnitude

    def applyEff(self, event, context): # Method to apply the effect
        if event == self.condition: # Check if the condition is met
            return self.effect(context, self.magnitude) # Apply the effect
        return context # Nothing Happens

class Character:
    def __init__(self, name, maxHp):
        self.name = name
        self.maxHp = maxHp
        self.Hp = maxHp
        self.block = 0
        self.potion = [None, None, None]
        self.relics = []
        self.buff = {'Strength': 0, 'Dexterity': 0}
    
    def relic_pickup(self, relic):
        self.relics.append(relic)

    def gain_block(self, amount):
        self.block += amount + self.buff['Dexterity']

    def damage_taken(self, damage):
        '''
        Handles damage taken by the character, applying block reduction and relic effects.
        '''
        damage = damage
        # Applies relic effects that reduce damage taken
        for relic in self.relics:
            damage = relic.applyEff('damageTaken', damage)
        self.block -= damage
        if self.block >= 0:
            return False
        else:
            damage = -self.block
            self.block = 0
            # Applies relic effects that reduce Hp Loss
            for relic in self.relics:
                damage = relic.applyEff('HpLoss', damage)
            self.Hp -= damage
        if damage > 0:
            return True
    
    def died(self):
        if self.Hp <= 0:
            for relic in self.relics:
                if relic.condition == 'dead' and relic.used == False:
                    self.Hp = relic.applyEff('dead', self.maxHp)
                    relic.used = True
                    return False
            return False
        else:
            return True

