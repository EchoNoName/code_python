def isPalindrom(word):
    if not word:
        return True
    elif len(word) == 1:
        return True
    elif len(word) in {2, 3}:
        if word[0] == word[-1]:
            return True
        else:
            return False
    else:
        if word[0] != word[-1]:
            return False
        else:
            return isPalindrom(word[1:-1])
    
print(isPalindrom('tacocat'))