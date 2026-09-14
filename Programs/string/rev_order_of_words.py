text = input("Enter a string: ")
words = text.split()


reverse_sentence = " ".join(words[ : :-1])

print(reverse_sentence)

for word in words [: : -1]:
    print(word, end=" ")


# print(text[::-1])