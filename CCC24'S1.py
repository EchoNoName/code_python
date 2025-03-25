n = int(input())
round_table = {}
for i in range(n):
    hat_num = int(input())
    round_table[i] = hat_num

out = 0

for i in range(n // 2):
    if round_table[i] == round_table[n // 2 + i]:
        out += 2

print(out)