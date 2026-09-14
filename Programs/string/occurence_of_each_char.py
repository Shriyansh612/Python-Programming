str = input("Enter a string: ")
l = len(str)
for i in range(0,255):
    c = 0
    for j in range(0,l):
        if (ord(str[j])==i):
            c+=1
    if (c>0):
        print (chr(i), ":", c)            