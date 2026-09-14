class Employee:
    def __init__(self,name,salary,bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def base_salary(self):
        return self.salary+self.bonus    

emp1 = Employee("Shriyansh",50000,5000)        
emp2 = Employee("Raghu",40000,6000)

print("Base salary of",emp1.name,"is",emp1.base_salary())
print("Base salary of",emp2.name,"is",emp2.base_salary())