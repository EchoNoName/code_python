def Chores(time, amt, args):
    if sum(args) <= time:
        return amt
    else:
        args = sorted(args)
        i = time - sum(args)
        while i > 0:
            i - args[-1]
            args.pop(-1)
        return len(args)
    
time = int(input())
amt = int(input())
chores = []
for i in range(amt):
    chores.append(int(input()))

print(Chores(time, amt, chores))