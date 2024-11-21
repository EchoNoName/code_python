i = int(input())
nums = []
for i in range(0, i):
    nums.append(2 * int(input()))

prime = [2]
for n in range(3, 2 * max(nums) - 2, 2):
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
    if isPrime:
        prime.append(n)
                
for i in nums:
    if i / 2 in prime:
        print(f"{int(i / 2)} {int(i / 2)}")
    else:
        for n in prime:
            found = False
            for p in prime:
                if n + p == i:
                    print(f"{n} {p}")
                    found = True
                    break
            if found:
                break