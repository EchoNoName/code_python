def binary_search(list, target, track = 0):
    if not list:
        return -1
    elif len(list) == 1 and list[0] != target:
        return -1
    else:
        left = 0
        right = len(list) - 1
        middle = (left + right) // 2
        if list[middle] == target:
            return track + middle
        elif list[middle] > target:
            return binary_search(list[:middle], target, track)
        else:
            return binary_search(list[middle + 1:], target, track + middle + 1)
        
list = [i for i in range(0, 100)]
print(binary_search(list, 101))