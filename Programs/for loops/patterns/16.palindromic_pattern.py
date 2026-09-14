length = int(input("Enter length: "))

for i in range(0,length):
    for k in range(length-i-1,0,-1):
        print(" ",end="")
    for j in range(i+1,0,-1):
        print(j,end="")
    if(i>0):
        for m in range(2,i+2):
            print(m,end="")       
    print()            