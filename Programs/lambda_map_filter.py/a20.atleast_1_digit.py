def atleast_1_digit(word):
    c=0
    for char in word:
        if(char.isdigit()):
            c+=1
    if(c>0):
        return True
    else:
        return False

words = ["hello","hello123","shriyansh","shriyansh612"]

filtered_words = list(filter(atleast_1_digit,words))
print(filtered_words)
