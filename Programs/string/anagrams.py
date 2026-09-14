str1 = input("Please enter a word: ")
str2 = input("Please enter a word: ")
l1 = len(str1)
l2 = len(str2)
c1 = 0
c2 = 0
for i in range (0,l1):
    if(not str1[i].isalpha()):
        c1+=1
for i in range (0,l2):
    if (not str2[i].isalpha()):
        c2+=1
if (len(str1.split())>1 or len(str2.split())>1):
    print("Please enter only one word")
elif (c1!=0 or c2!=0):
    print("Please enter only alphabets in the word")
else:
     new_str1 = ""
     new_str2 = "" 
     for i in range (97,123):
         for j in range(0,l1):
             if (ord(str1[j])==i or ord(str1[j])==i-32):
                 new_str1=new_str1+str1[j]
         for k in range(0,l2):
             if (ord(str2[k])==i or ord(str2[k])==i-32):
                 new_str2=new_str2+str2[k]           
     if (new_str1==new_str2):
        print("They are anagrams")
     else:
        print("They are not anagrams")
                 
