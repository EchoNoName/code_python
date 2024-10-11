def palindrome(word):
    '''determains if a word is a palindrome
    
    args:
        word: A string that only contains alphabetical characters
    
    returns: 
        A true or false value representing wether a word is a palindrome
    '''
    return(word.lower() == word.lower()[::-1])

print(palindrome('Tacocat'))