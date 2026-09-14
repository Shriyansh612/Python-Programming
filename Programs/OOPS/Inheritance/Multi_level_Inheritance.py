class Grandparent:
    def display(self):
        print("Grandparent")

class Parent(Grandparent):
    def display1(self):
        print("Parent")

class Child(Parent):
    def display2(self):
        print("Child")        

obj1 = Child()        
obj1.display2()
obj1.display1()
obj1.display()