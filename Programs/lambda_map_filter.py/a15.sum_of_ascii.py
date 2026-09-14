def sum_ascii(word):
    sum=0
    for char in word:
        sum+=ord(char)
    return sum

words = ["hello","computer","hi","mouse"]
print(list(map(lambda word:[word,sum_ascii(word)],words)))    