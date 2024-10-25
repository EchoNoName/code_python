def factorList(num):
    '''determains all factors of a number
    
    args:
        num: an integer value
        
    return
        factor: a list of factors of the num'''
    factor = [1]
    for i in range(2, num):
        if num % i == 0:
            factor.append(i)
    factor.append(num)
    return factor

print(factorList(12))

def isPrime(num):
    '''determains if a number is prime
    
    args:
        num: an integer
    
    returns:
        a True or False on whether num is prime'''
    #I can also write
    # factor = factorList(num)
    # if len(factorList) == 2:
    #     return True
    # else: 
    #     return False
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, num):
            if num % i == 0:
                return False
    return True

print(isPrime(12))