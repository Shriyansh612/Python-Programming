text = input("Enter a string: ")
c1=0    #digits
c2=0    #upper
c3=0    #lower
c4=0    #special symbols
c5=0    #spaces
for char in text:
    if (char.isdigit()):
        c1+=1
    elif (char.isalpha()):
        if (char.islower()):
            c3+=1
        else:
            c2+=1
    elif (char==" "):
        c5+=1
    else:
        c4+=1
print("Number of digits:", c1)                            
print("Number of upper:", c2)                            
print("Number of lower:", c3)                            
print("Number of special symbols:", c4)                            
print("Number of spaces:", c5)                            
