def divide(list):
    if not list:
        return -1
    elif len(list) == 1:
        return list
    else:
        return divide(list[:len(list)//2]), divide(list[len(list)//2:])

def merge(Left, Right):
    k = 0
    i = 0
    j = 0
    arr = []
    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            arr.append(Left[i])
            i += 1
            k += 1
        else:
            arr.append(Right[j])
            j += 1
            k += 1
    
    while i < len(Left):
        arr.append(Left[i])
        i += 1
        k += 1
    
    while j < len(Right):
        arr.append(Right[j])
        j += 1
        k += 1
    
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]

        merge_sort(Left)
        merge_sort(Right)

        k = 0
        i = 0
        j = 0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = (Right[j])
                j += 1
            k += 1
        
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
        
        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

list = [2, 3, 4, 1, 7, 8, 9, 1, 11]
merge_sort(list)
print(list)