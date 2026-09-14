m1 = int(input("Enter your maths marks: "))
m2 = int(input("Enter your science marks: "))
m3 = int(input("Enter your english marks: "))
m4 = int(input("Enter your hindi marks: "))

def average(m1,m2,m3,m4):
    return((m1+m2+m3+m4)/4)

def percentage(m1,m2,m3,m4):
    print((m1+m2+m3+m4)/400*100,"%")

def total_marks(m1,m2,m3,m4):
    print(m1+m2+m3+m4)

def division ():
    percentage=average(m1,m2,m3,m4)
    if (percentage>=80):
        print("First Division")
    elif(percentage>=60):
        print("Second Division")
    elif(percentage>=40):
        print("Third Division")
    else:
        print("Fail")

operation=""
print('''
Enter \'a\' for average
Enter \'t\' for total marks
Enter \'p\' for percentage
Enter \'d\' for division
Enter \'e\' to end the program''')
while(operation!="e"):
    operation=input()
    match operation:
        case "a":
            print(average(m1,m2,m3,m4))
        case "t":
            total_marks(m1,m2,m3,m4)
        case "p":
            percentage(m1,m2,m3,m4)
        case "d":
            division()
        case _:
            print("Please enter valid input")                
