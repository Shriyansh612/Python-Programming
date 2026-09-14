class Student:
    class_marks = {}
    def __init__(self,name,age,marks,city):
        self.name = name
        self.age = age
        self.marks = marks
        self.city = city
        Student.class_marks[self.name]=self.marks

s1 = Student("Shriyansh",19,70,"Agra")
s2 = Student("Raghu",17,80,"Agra")
s3 = Student("Ravi",18,50,"Agra")
s4 = Student("Priyanshu",17,60,"Agra")
s5 = Student("Mannu",16,90,"Agra")

marks = sorted(Student.class_marks.values())
print()

lowest = ""
highest = ""
above80 = []
below40 = []

for key in Student.class_marks:
    if (Student.class_marks[key]==marks[0]):
        lowest = key
    if (Student.class_marks[key]==marks[-1]):
        highest = key
    if (Student.class_marks[key]>80):
        above80.append(key)
    if (Student.class_marks[key]<40):
        below40.append(key)               

average = sum(marks)/len(marks)

print("Highest marks:",Student.class_marks[highest],highest)
print("Lowest marks:",Student.class_marks[lowest],lowest)
print("Students scoring above 80:",*above80)
print("Students scoring below 40:",*below40)
print("Average of class:",average)
