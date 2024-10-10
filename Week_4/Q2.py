def cleaner(word):
    '''Cleans up a string to get rid of non-alphabeticle characters and lowercase the string
    
    args:
        word: A String that can contain alpha-numeric characters and special characters
        
    returns: 
        cleaned_string: a string that had all of its non-alphabetical characters removed
    '''
    cleaned_string = ''
    for i in word:
        if i.isalpha():
            cleaned_string += i
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

print(cleaner("H E LL  O 091 !!!"))