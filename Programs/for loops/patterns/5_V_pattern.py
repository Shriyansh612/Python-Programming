height = input("Enter height of V pattern: ")
if (not height.isdigit()):
    print ("Please enter digit")
elif (int(height)<3):
    print("Please enter height of atleast three")
else: 
    height = int(height)       
    for i in range (1,height+1): # for rows
        for j in range (1,2*height):  #for columns 
            if (j==i or j==2*height-i):   # to print * at diagonal places
                print("*", end="")
            else:
                print(" ", end = "")
        print("")            