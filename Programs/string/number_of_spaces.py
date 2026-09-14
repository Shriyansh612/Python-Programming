str = input("Enter a string: ")
l = len(str)
c = 0
for i in range(0,l):
    if (str[i]==" "):
        c+=1
print("Number of spaces in the string is", c)        