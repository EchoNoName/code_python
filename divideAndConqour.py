def divideAndConquer(arr: list):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[mid:]
        right = arr[:mid]
        return divideAndConquer(left), divideAndConquer(right)

print(divideAndConquer([9, 4, 1, 5, 6, 11, 18, 19, 1, 1, 8]))
