marks =  input("Enter marks: ")
if (marks.isdigit()):
    marks = int(marks)
    if (marks>100 or marks<0):
        print("Please enter valid marks")
    elif (marks>=90):
        print("grade: A")
    elif (marks>=80):
        if (marks>=85):
            print("Grade: A-")
        elif (marks>=80):
            print("Grade : B+")
    elif (marks<80):
        if (marks>=70):
            print("Grade: C")
        elif(marks>=33):
            print("Grade: D")
        else:
            print("Grade: F")     
else:
    print("Please enter digits")            

