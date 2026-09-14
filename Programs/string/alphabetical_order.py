str = input("Enter a word: ")
l = len(str)
c = 0
for i in range (0,l):
    if (not str[i].isalpha()):
        c += 1
if(len(str.split())>1):
    print("Please enter only one word")
elif (c!=0):
    print("Please enter only alphabets in the word")
else:    
    str_new = ""
    for i in range (97, 123):
        for j in range (0,l):
            if (ord(str[j])==i or ord(str[j])==i-32):
                str_new = str_new+str[j]
    print(str_new)                