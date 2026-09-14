str = input("Enter a string: ")
l = len(str)
d = 0
for i in range(97,123):
    c = 0
    for j in range (0,l):
        if(ord(str[j].lower())==i):
            c+=1
    if(c>d):
        d = c   
for i in range(97,123):
    c = 0
    for j in range (0,l):
        if(ord(str[j].lower())==i):
            c+=1
    if (c==d):
        print("Most frequent character is:", chr(i), ":", d)     