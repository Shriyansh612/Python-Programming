class Parent1:
    def display1(self):
        print("Parent1")

class Parent2:
    def display2(self):
        print("Parent2")        

class Child(Parent1,Parent2):
    def display(self):
        print("Child")        

obj1 = Child()        
obj1.display()
obj1.display1()
obj1.display2()