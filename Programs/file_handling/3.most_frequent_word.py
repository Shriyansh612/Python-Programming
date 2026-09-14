file = open(r"programs\file_handling\data.txt","r")
words = file.read().split()
file.close()

max_word = words[0]
count = words.count(words[0])

for word in words:
    if (words.count(word)>count):
        count = words.count(word)
        max_word = word

print(f"Word having highest frequency is \"{max_word}\" and its frequency is {count}")



"""
i am rohit
i am learning python
i am from agra
i love python
"""
