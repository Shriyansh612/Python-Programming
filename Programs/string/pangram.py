text = input("Enter a string: ")
c=0
for i in range(97,123):
    for j in range (0,len(text)):
        if (chr(i)==text[j] or chr(i-32)==text[j]):
            c+=1
            break
if(c==26):
    print("It is a pangram")
else:
    print("It is not a pangram")            

