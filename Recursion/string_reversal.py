def reverse(word):
    if not word:
        return False
    elif len(word) == 1:
        return word
    elif len(word) == 2:
        return word[-1] + word[0]
    else:
        return word[-1] + reverse(word[1:-1]) + word[0]
    
print(reverse('123456789'))

def reverseTail(word, tailS = "", tailE = ""):
    if not word:
        return False
    elif len(word) == 1:
        return tailS + word + tailE
    elif len(word) == 2:
        tailS += word[-1]
        tailE = word[0] + tailE
        return tailS + word + tailE
    else:
        tailS += word[-1]
        tailE = word[0] + tailE
        return reverseTail(word[1:-1], tailS, tailE)

print(reverseTail("123456789"))