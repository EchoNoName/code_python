def factorCounter(num):
    '''determains the # of factors an integer has
    
    args: 
        num: an Integer value
    
    returns: 
        factor: an Integer representing the # of factors num has
    '''
    factor = 2
    for i in range(2, num):
        if num % i == 0:
            factor += 1
    return (factor)

print(factorCounter(int(input("Enter a Integer: "))))