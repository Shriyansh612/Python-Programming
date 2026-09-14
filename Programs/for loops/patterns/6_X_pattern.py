height = input("Enter height which is an odd number of X pattern: ")
if (not height.isdigit()):
    print ("Please enter digit")
elif (int(height)<3):
    print("Please enter height of atleast three")
elif (int(height)%2==0):
    print("Please enter odd height")
else:
    height = int(height)
    for i in range(1,height+1):
        for j in range(1,height+1):
            if (i==j or j==height-i+1):
                print("*",end= "")
            else:
                print(" ", end ="")
        print("")                    