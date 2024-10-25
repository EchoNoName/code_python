def isPalindrome(word):
    '''determains if a word is a palindrome
    
    args:
        word: A string that only contains alphabetical characters
    
    returns: 
        A true or false value representing wether a word is a palindrome
    '''
    if not word:
        return True
    elif len(word) == 1:
        return True
    elif len(word) <= 3:
        if word[0] == word[-1]:
            return True
        else:
            return False
    else:
        for i in range(len(word) // 2):
            if word[i] != word[-i - 1]:
                return False
    return True

print(isPalindrome('tacocat'))