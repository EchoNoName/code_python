def PSA(list):
    ''' This function takes and array of numbers and converts it into a Prefix Sum Array used for finding the sum of numbers in an array from i - j inclusive

    Args: a list of numbers

    Returns: PSA of the list

    '''
    psa = []
    psa.append(list[0])
    for i in range(1, len(list)):
        psa.append(list[i] + psa[i - 1])
    return psa

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
psa = PSA(nums)
print(nums)
i = int(input("Enter index i: "))
j = int(input("Enter index j: "))
if i == 0:
    print(psa[j])
else:
    print(psa[j] - psa[i - 1])
