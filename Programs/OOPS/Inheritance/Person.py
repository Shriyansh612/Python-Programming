# supar method --> super() method is used to access method of the parent class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name, age,roll,course):
        super().__init__(name, age)
        self.roll = roll
        self.course = course
        
    def display(self):
        print(self.name)        
        print(self.age)        
        print(self.roll)        
        print(self.course)        

# stu1 = Person("Shriyansh",19)
stu1 = Student("aman",19,101,"maths")        
stu1.display()
