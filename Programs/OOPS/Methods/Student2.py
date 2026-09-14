class student:

    college = "IIT BHU"

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks


    #instance method
    def student_details(self):
        print("Name:",self.name)    
        print("Marks:",self.marks)

    #class method
    @classmethod
    def change_college(cls):
        cls.college = input("Enter new college name:") 

    #static_method
    @staticmethod
    def valid_marks(marks):
        if 0 <= marks <= 100:
            return True
        else:            
            return False

# calss static method
s1 = student("Shriyansh",80)

#calling instance method
s1.student_details()

#calling class method

student.change_college()

#calling static method
print(student.valid_marks(s1.marks))
