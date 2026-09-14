text = input("Enter string: ")
length = len(text)
if (length%2!=0):
    print("False")
else:
    count=0
    for char in text:
        if (not char in "(){}[]"):
            count+=1
            break
    if (count==1):
        print("false")
    else:
        brackets=[]     
        for char in text:
            brackets.append(char)
        print(brackets)           
