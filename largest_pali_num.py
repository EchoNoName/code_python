def largestPaliNum():
    i = 99
    paliNum =[0]
    for x in range(999, 99, -1):
        #only break out of second loop incase there is a the first pali found is like 999 * 500 and 998 * 800 is also a pali.
        for y in range(999, i, -1):
            num = x * y
            if str(num) == str(x * y)[::-1]:
                i = y
                paliNum.append(x * y)
                break
            elif num < max(paliNum):
                i = y
                break
    return max(paliNum)

print(largestPaliNum())