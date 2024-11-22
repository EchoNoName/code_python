import math



def small_damage_reduction(damage, cap, *args): # The reduce small damage to 1 effect
    if damage <= cap and damage > 1:
        return 1

def hp_loss_reduction(hp_loss, reduction): # Hp Loss Reduction Effect
    return hp_loss - reduction

def revive(revive_percentage, max_hp):
    return math.floor(max_hp * (revive_percentage / 100))