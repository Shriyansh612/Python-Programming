password = input("Enter password: ")
count=0     #spaces
for i in range(0,len(password)):
    if(password[i]==" "):
        count+=1
if (count>0):
    print("Spaces are not allowed in password")
elif(len(password)<=8):
    print("Password must be at least of 8 characters")    
else:
    count1=0    #digit
    count2=0    #lower
    count3=0    #upper
    count4=0    #special symbols
    for i in range (0,len(password)):
        if (password[i].isdigit()):
            count1 += 1
        elif (password[i].islower()):
            count2 += 1
        elif (password[i].isupper()):
            count3 += 1 
        else:
            count4 += 1 
    if (count1>0 and count2>0 and count3>0 and count4>0 and len(password)>=12):
        print("Strong Password")
    elif(count1>0 and count2>0 and count3>0):
        print("Medium Password") 
    elif (count1>0 or count2>0):
        print("Weak Password")
    else:
        print("Medium Password")     
    
    