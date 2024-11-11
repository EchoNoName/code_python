def isPrime(x, divisor = None):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        if divisor == None:
            divisor = 2
        if divisor > x ** 0.5:
            return True
        if x % divisor != 0:
            return isPrime(x, divisor + 1)
        else:
            return False

print(isPrime(1223))