
def func(n):
    ans = 0
    for a in range(n // 4 + 1):
        for b in range(n // 5 + 1):
            if a * 4 + b * 5 == n:
                ans += 1
    return ans

for i in range(1, 21):
    print(func(i))