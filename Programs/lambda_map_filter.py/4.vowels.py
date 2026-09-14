def vowels2(word):
    c=0
    for chr in word:
        if (chr in'aeiou'):
            c+=1
    if(c>2):
        return word

words = ["hello","nature","mathematics","computer","normal"]

print(list(filter(vowels2,words)))