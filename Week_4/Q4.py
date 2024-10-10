def consonantCounter(text):
    '''Determaisn the # of consonants a word has including y
    
    args: 
        text: a string containing alpha-numeric characters and special characters
    
    returns:
        cons_count: a # representing the # of consonats in text
    '''
    cons_count = 0
    for i in text:
        if i.isalpha() and i not in {'a', 'e', 'i', 'o', 'u'}:
            cons_count += 1
    
    return(cons_count)

print(consonantCounter("blueberry"))