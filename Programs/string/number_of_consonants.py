str = input("Enter string: ")
l = len(str)
c = 0
for i in range(0,l):
    if(str[i].isalpha()):
        if(not str[i].lower() in 'aeiou'):
            c += 1
print("Number of Consonants:", c)             