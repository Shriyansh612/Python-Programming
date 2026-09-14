class Restaurant:
    def __init__(self):
        self.name = input("Enter name of restaurant: ")

class Pizza_Restaurant(Restaurant):
    def __init__(self):
        self.price = int(input("\nEnter price of pizza: "))
        self.tax_percent = float(input("Enter tax percent: ")) 
        self.quantity = int(input("Enter how many pizzas do you want: "))            
        
    def Calculate_Bill(self):
        self.bill = self.price*self.quantity*(1+self.tax_percent/100)
        self.tax = self.bill-self.price*self.quantity
        print("Bill: ",self.bill)        
        print("Tax: ",self.tax)

class Burger_Restaurant(Restaurant):
    def __init__(self):
        self.price = int(input("\nEnter price of burger: "))
        self.tax_percent = float(input("Enter tax percent: ")) 
        self.quantity = int(input("Enter how many burgers do you want: "))

    def Calculate_Bill(self):
        self.bill = self.price*self.quantity*(1+self.tax_percent/100)
        self.tax = self.bill-self.price*self.quantity
        print("Bill: ",self.bill)        
        print("Tax: ",self.tax)

class Indian_Restaurant(Restaurant):
    def __init__(self):
        self.price = int(input("\nEnter price of thali: "))
        self.tax_percent = float(input("Enter tax percent: ")) 
        self.quantity = int(input("Enter how many thalis do you want: "))
        self.discount_percent = float(input("Enter discount percent: "))                           

    def Calculate_Bill(self):
        self.bill = self.price*self.quantity*(1+self.tax_percent/100)*(1-self.discount_percent/100)    
        self.tax = self.price*self.quantity*self.tax_percent/100
        self.discount = self.price*self.quantity*(1+self.tax_percent/100)*(self.discount_percent/100)
        print("Bill: ",self.bill)
        print("Tax: ",self.tax)
        print("Discount: ",self.discount)

def Bill(obj):
    obj.Calculate_Bill()        

pizza = Pizza_Restaurant()  
Bill(pizza)  
burger = Burger_Restaurant()
Bill(burger)
thali = Indian_Restaurant()
Bill(thali)