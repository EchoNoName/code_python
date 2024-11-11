def findMax(list):
    if not list:
        return False
    elif len(list) == 1:
        return list[0]
    elif len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]
    else:
        if list[-1] > list[-2]:
            list.pop(-2)
        else:
            list.pop(-1)
        return findMax(list)

print(findMax([6, 1, 3, 8, 10, 26, 55, 19, 3, 7, 71, 102, 0, 12, -12]))