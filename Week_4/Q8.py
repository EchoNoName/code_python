def meanMedFinder(numList: list):
    '''Determains the mean and median of a list of integers
    
    args: 
        numList: A list of integers
    
    returns:
        mean: the mean of the list of integers
        median: the median of the list of integers'''
    numList = sorted(numList)   
    med = 0
    if len(numList) % 2 == 0:
        med = (numList[len(numList)] + numList[len(numList) - 1]) / 2
    else:
        med = (numList[len(numList) // 2])
    mean = sum(numList) / len(numList)
    return (mean, med)

meanMed = meanMedFinder([1, 1, 2, 3, 4, 5, 7, 7, 7])
print(f"The mean is {meanMed[0]}")
print(f"the median is {meanMed[1]}")


