class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.roll = input("Enter your roll number: ")
        self.course = input("Enter your course: ")

    def get_data(self):
        print("\nData:")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Roll No:", self.roll)
        print("Course :", self.course)


students = []

for i in range(5):
    print(f"\nEnter details of Student {i + 1}")
    students.append(Student())

print("\n----- All Student Details -----")

for students in students:
    students.get_data()                   