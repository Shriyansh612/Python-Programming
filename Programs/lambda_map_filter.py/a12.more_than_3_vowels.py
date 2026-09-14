def more_than_3_vowels(word):
    c=0
    for char in word:
        if(char in'aeiou'):
            c+=1
    if(c>3):
        return True
    else:
        return False

words = ["education","computer","illustrations","hello"]

filtered_words = list(filter(more_than_3_vowels,words))
print(filtered_words)

