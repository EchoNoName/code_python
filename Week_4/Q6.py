def anagram(text1, text2):
    '''determains if 2 words are anagrams
    
    args: 
        text1: the first word
        text2: the second word
        
    returns:
        True: if the 2 words are anagrams
        False: if the 2 words are not anagrams
    '''
    if len(text1) != len(text2):
        return False
    else:
        text1 = sorted(text1)
        text2 = sorted(text2)
        for i, c in enumerate(text1):
            if text2[i] != c:
                return False
    return True

print(anagram('bored', 'robed'))