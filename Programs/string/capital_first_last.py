text = input("Enter string: ")
words = text.split()
for word in words:
    word = word.capitalize()
    word = word[:-1]+word[-1].upper()
    print(word)

# str = "Hello"

# print(str.replace([-1],"*"))