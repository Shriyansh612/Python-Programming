length = int(input("Enter length: "))
for i in range(1,length+1):
    for k in range(length-i,0,-1):
        print(" ",end="")
    for j in range(i):
        print(i," ",end="")
    print()        