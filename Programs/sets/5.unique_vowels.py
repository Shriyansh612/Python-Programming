text = input("Enter text: ")
letters = set(text.lower())
vowels = set(filter(lambda char : char in "aeiou",letters))
print(vowels)