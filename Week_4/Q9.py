from random import randrange

def stringToIntList(text):
    '''Converts a string of numbers seperated by commas to a list of numbers
    
    args: 
        text: A string of numbers seperated by commas
        
    returns:
        nums: A list of numbers
    '''
    nums = text.split(',')
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    return nums

print(stringToIntList("1,2,3,4,5"))

def randList(start, end, frequency):
    '''Creates a list of x many numbers in a certain range
    
    args: 
        start: the min of the range of numbers that can be generated
        end: the max of the range of numbers
        frequency: the # of numbers to be generated
        
    returns: A list of numbers'''
    nums = []
    for i in range(frequency):
        nums.append(randrange(start, end + 1))   
    return nums

print(randList(0, 1000, 20))