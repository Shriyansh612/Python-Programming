maths = int(input("Enter maths marks: "))
physics = int(input("Enter physics marks: "))
chem = int(input("Enter chem marks: "))
bio = int(input("Enter bio marks: "))
computer = int(input("Enter computer marks: "))



if(maths < 0 or maths > 100 or
physics < 0 or physics > 100 or
chem < 0 or chem > 100 or
bio < 0 or bio > 100 or
computer < 0 or computer > 100):

    print("Invalid marks! marks should be between o and 100.")

elif (maths < 33 or physics < 33 or chem  < 33 or bio < 33 or computer < 33):
    print("Fail")
    print("Percentage:", (maths+physics+chem+bio+computer)/5)

else:
    average = (maths + physics + chem + bio + computer)/5
    print ("Percentage: ", average)  
    if (average>=90):
        print("A")
    elif (average>=80):
        print("B")
    elif (average>=70):
        print("C")
    elif (average>=60):
        print("D")
    elif (average>=40):
        print("E")
    elif (average<40):
        print("F")                