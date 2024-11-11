def exponential(base, power):
    if base == 0:
        return 0
    elif base == 1:
        return 1
    elif power == 0:
        return 1
    elif power == 1:
        return base
    else:
        return base * exponential(base, power - 1)
    
def exponentialTail(base, power, tail = 1):
    tail *= base
    if base == 0:
        return 0
    elif base == 1:
        return 1
    elif power == 0:
        return 1
    elif power == 1:
        return tail
    else:
        return exponentialTail(base, power - 1, tail)
    
print(exponential(26, 24))
print(exponentialTail(26, 24))