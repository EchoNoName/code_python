def patternMaker(n):
    '''Creates a pattern based on an inputed intger
    
    args: 
        n: # of lines the pattern goes on for
        
    returns:
        pattern: The full pattern the fuction makes, starting of with the number of lines, then n lines of alternating 1s and 0s that are the length of the line #'''
    line = ''
    pattern = f"N = {n} \n\n"
    for i in range(n):
        if i % 2 == 0:
            line += '1'
        else:
            line += '0'
        pattern += f'{line} \n'
    return(pattern)

print(patternMaker(5))