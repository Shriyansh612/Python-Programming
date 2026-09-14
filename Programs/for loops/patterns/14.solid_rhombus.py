length = int(input("Enter length: "))

for i in range(length):
    for j in range(2*length-1):
        if(length-1<=i+j<=2*length-2):
            print("*",end="")
        else:
            print(" ",end="")    
    print()        