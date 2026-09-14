hor = int(input("Enter horizontal length"))
ver = int(input("Enter vertical length"))
for i in range(1,ver+1):
    for j in range(1,hor+1):
        if (i==1 or j==1 or i==ver or j==hor):
            print("*", end="")
        else:
            print(" ", end="")
    print("")            