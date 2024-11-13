def GCF(num1, num2):
    if num1 > num2:
        max = num1
        min = num2
    else:
        max = num2
        min = num1
    if max % min == 0:
        return min
    else:
        for i in range(min // 2, 0, -1):
            if max % i == 0 and min % i == 0:
                return i
            
print(GCF(182, 247))

def GCF_r(num1, num2, divisor = 0):
    if divisor == 0:
        divisor = min(num1, num2)
    if divisor == 1:
        return 1
    elif num1 % divisor == 0 and num2 % divisor == 0:
        return divisor
    else:
        return GCF_r(num1, num2, divisor - 1)

print(GCF_r(182, 247))

def GCF_e(a, b):
    if b == 0:
        return a
    else:
        return GCF_e(b, a % b)

print(GCF_e(128, 56))