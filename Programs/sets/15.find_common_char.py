str1 = input("Enter text: ")
str2 = input("Enter text: ")

common = set()

for char in str1:
    if(char in str2):
        common.add(char)

print(common)        