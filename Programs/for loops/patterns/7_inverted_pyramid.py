height = int(input("Enter height: "))
for i in range (1, height+1):
    for j in range (1, 2*height-i+1):
        if (j>=i):
            print("*", end="")
        else :
            print(" ", end="")
    print("")            