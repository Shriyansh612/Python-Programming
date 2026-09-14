height = int(input("Enter height of diamond: "))
upper = height//2
for i in range (1,upper+1):
    print(" ", end="")
    for j in range (1,upper+i):
        if (j>=(upper-i+1)):
            print("*", end="")
        else:
            print(" ", end= "")
    print("")
lower = height-upper                    
for i in range (1, lower+1):
    for j in range (1, 2*lower-i+1):
        if (j>=i):
            print("*", end="")
        else :
            print(" ", end="")
    print("")            


print("\n\n")

for i in range(1,height+1):
    for j in range (1,height+1):
        if (i+j>=(height//2)*2 and i+j<=(height//2)*2+height-1 and j-i<=height//2 and j-i>=-(height//2)):
            print("*", end="")
        else:
            print(" ", end="")
    print("")                