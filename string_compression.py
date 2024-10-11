def txt_comp(word):
    ctr = 1
    comp_word = ''

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            ctr += 1
        else:
            comp_word += f"{word[i-1]}{ctr}"
            ctr = 1
    comp_word += f"{word[i-1]}{ctr}"

    if len(comp_word) < len(word):
        return comp_word
    else:
        return word

word = input("Enter a String to be compressed")
print(txt_comp(word))