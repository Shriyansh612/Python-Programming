str = input("Enter string: ")
str1 = str.split()
l = len(str1)
c = 0     #Counter to check whether word is only of alphabets  
n = 0     #Number of words
for i in range(0,l):
    word = str1[i]
    l1 = len(word)
    for j in range (0,l1):
        if (word[j].isalpha()):
            c+=1
    if (c==l1):
        n+=1
    c = 0            
             
print ("Number of words in the string:", n)