str = input("Enter string: ")
c = 0
l = len(str)
for i in range (0,l):
    if (str[i] in 'aeiou'):
        c+=1
print("Number of vowels:", c)        