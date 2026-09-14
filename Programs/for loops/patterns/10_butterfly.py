length = int(input("Enter length: "))

for i in range(2*length):
    for j in range(2*length):
        if (i<=length-1):
            if (i-j>=0 or i+j>=7):
                print("*",end="")
            else:
                print(" ",end="")
        else:
            if(i+j<=7 or i-j<=0):
                print("*",end="")
            else:
                print(" ",end="")
    print()                                    