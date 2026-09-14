# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self,brand,model,number_of_doors):
#         super().__init__(brand,model)
#         self.number_of_doors = number_of_doors

#     def display(self):
#         print(self.model)        
#         print(self.brand)        
#         print(self.number_of_doors)        


# c1 = Car("Toyota","Innova",4)
# c1.display() 




# class Parent1:
#     def __init__(self):
#         print("Parent1 constructor")


# class Parent2:
#     def __init__(self):
#         print("Parent2 constructor")


# class Child(Parent2, Parent1):
#     def __init__(self):
#         Parent1.__init__(self)
#         Parent2.__init__(self)
#         # super().__init__()
#         print("Child constructor")


# obj = Child()


class Vehicle:
    def __init__(self,brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self,model,number):
        self.model = model
        self.number = number
        brand = input("Enter brand: ")
        super().__init__(brand)

class Rental_Car(Car):
    def __init__(self):
        model = input("Enter model number: ")     
        number = input("Enter number: ")
        super().__init__(model,number)
        self.rented = False
        self.days = 0
        self.cost = 0
        


    def rent_car(self):
        if (self.rented==False):
            self.rented = True
            self.rent = int(input("Enter rent of one day: "))
            self.days = int(input("For how many days would you like to rent the car: "))
            print("Cost:",self.days*self.rent)
            # self.cost = self.rent*self.days
            print("Car rented\n")
        else:
            print("The car is already rented\n")            

    def return_car(self):
        self.late_return = bool(int(input("Enter 1 if late return else 0: ")))
        if (self.rented):
            self.rented = False
            print("Bill:")
            self.calc_cost()                    
            print(self.cost)

        else:
            print("The car is not rented\n")
    
    def calc_cost(self):
        if (self.late_return):
            self.cost = self.rent*self.days*1.2
        else:
            self.cost = self.rent*self.days

car1 = Rental_Car()
car1.rent_car()            
car1.return_car()