n = int(input())

solution = {
    0: 1,
    1: 0,
    2: 0,
    3: 0,
    4: 1,
    5: 1,
    6: 0,
    7: 0,
    8: 1,
    9: 1,
    10: 1,
    11: 0,
    12: 1,
    13: 1,
    14: 1,
    15: 1,
    16: 1,
    17: 1,
    18: 1,
    19: 1,
    20: 2
}

if n <= 20:
    print(solution[n])
else:
    print(n // 20 + solution[n % 20])