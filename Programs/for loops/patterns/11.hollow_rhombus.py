length = int(input("Enter length of rhombus: "))

for i in range(length):
    for j in range(2*length-1):
        if (i==0 and (length-1)<=j<=(2*length-2)):
            print("*",end="")
        elif (i==length-1 and j<=length-1):
            print("*",end="")
        elif (i+j==4 or i+j==8):
            print("*",end="")
        else:
            print(" ",end="")    
    print()                                        