def isPalindrome(word):
    '''determains if a word is a palindrome
    
    args:
        word: A string that only contains alphabetical characters
    
    returns: 
        A true or false value representing wether a word is a palindrome
    '''
    return(word == word[::-1])

print(isPalindrome('tacocat'))