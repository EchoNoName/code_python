def stringDupes(word1, word2):
    '''Finds duplicate characters in 2 strings
    
    args:
        word1: the first string to be inputted
        word2: the second string to be inputted
        
    returns:
        dupes: a list of all duplicate characters between the 2 strings'''
    dupes = [i for i in word1 if i in set(word2)]
    return dupes

print(stringDupes('hello', 'goodbye'))