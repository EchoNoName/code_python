n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

for number in nums:
    for i in range(number + 1, 2 ** 26, 1):
        if isinstance(i ** 3, int) and str(int(i ** 3)).endswith('888'):
            print(i)
            break