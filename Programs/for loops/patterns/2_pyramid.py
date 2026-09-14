height = int(input("Enter height of pyramid: "))
for i in range (1,height+1):
    for j in range (1,height+i):
        if (j>=(height-i+1)):
            print("*", end="")
        else:
            print(" ", end= "")
    print("")                

