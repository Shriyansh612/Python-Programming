text = input("Enter a string: ")
c1 = 0      #alphabets
c2 = 0      #digits
c3 = 0      #special symbols
for char in text:
    if(char.isalpha()):
        c1+=1
    elif(char.isdigit()):
        c2+=1
    elif(not char==" "):
        c3+=1         
if (c1>0 and c2==0 and c3==0):
    print("The string has only alphabets")        
elif (c1==0 and c2>0 and c3==0):
    print("The string has only digits")        
elif (c1==0 and c2==0 and c3>0):
    print("The string has only symbols")        
elif (c1>0 and c2>0 and c3==0):
    print("The string has both alphabets and digits")        
elif (c1==0 and c2>0 and c3>0):
    print("The string has both digits and symbols")        
elif (c1>0 and c2==0 and c3>0):
    print("The string has both alphabets and symbols")        
elif (c1>0 and c2>0 and c3>0):
    print("The string has all alphabets, digits and symbols")  
else:
    print("Please enter something")     