def nthFactor(i: int, k: int):
    factor = [1, i]
    for n in range(2, int(i ** (1/2)) + 1):
        if i % n == 0:
            factor.append(n)
            if i // n != n:
                factor.append(i // n)
    factor.sort()
    if len(factor) < k:
        return -1
    else:
        return factor[k - 1]
    
print(nthFactor(16, 3))