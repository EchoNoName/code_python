def golf(goal, *args):
    args = list(args)
    strokes = 1
    if args.count(goal) == 1:
        return strokes
    possible = args
    while True:
        strokes += 1
        temp = []
        for i in possible:
            for u in args:
                temp.append(i + u)
        possible = temp
        for i in possible:
            if i > goal:
                possible.remove(i)
        if possible.count(goal) > 0:
            return strokes
        else:
            if not possible:
                return False

print(golf(10100, 34, 66, 1))