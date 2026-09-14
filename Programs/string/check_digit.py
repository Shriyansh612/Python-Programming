str = input("Enter string: ")
l = len(str)
c = 0
for i in range (0, l):
    if (str[i].isdigit()):
        c+=1
if (c>0):
    print(f"The string contains {c} number of digits")
else:
    print("The string does not contains any digits")            