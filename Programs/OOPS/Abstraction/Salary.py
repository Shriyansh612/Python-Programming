class Salary: 
    def __init__(self):
        self.name = input("Enter your name: ")
        self.__salary=0
        salary = int(input("Enter your salary: "))
        if (salary<0):
            print("Negative salary is not allowed")
        else:
            self.__salary = salary    

    def give_raise(self,percent):
        self.__salary=self.__salary*(1+percent/100)       

    def get_salary(self):
        return self.__salary

person1 = Salary()        
person1.give_raise(20)
print(person1.get_salary())