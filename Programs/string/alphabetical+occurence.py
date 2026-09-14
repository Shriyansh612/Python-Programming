str = input("Enter a string: ")
l = len(str)
new_str = ""
for i in range (97,123):
    c = 0
    for j in range (0,l):
        if (ord(str[j].lower())==i):
            c = c+1
    if (c>0):            
        new_str = new_str + chr(i)
        print(chr(i),":",c)
print(new_str)        