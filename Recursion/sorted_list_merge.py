def mergeSortedList(list1, list2):
    if not list1:
        if not list2:
            return False
        else:
            return list2
    elif not list2:
        return  list1
    else:
        if list1[0] < list2[0]:
            return [list1[0]] + mergeSortedList(list1[1:], list2)
        else:
            return [list2[0]] + mergeSortedList(list1, list2[1:])
        
print(mergeSortedList([1, 5, 9, 10], [2, 4, 7, 11]))