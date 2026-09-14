class Product:
    def __init__(self):
        self.name = input("Enter name of product: ") 
        self.__price = int(input("Enter price: "))
        self.__discount = int(input("Enter discount percent: "))
        self.flag = 0

        if (self.__price<0):
            print("Price must be greater than zero")
            self.flag=1
            
        if not(0<=self.__discount<=50):
            print("Discount percentage must be between 0 and 50")
            self.flag=1
            
        

    def final_price(self):
        if(self.flag==0):
            self.__price = self.__price*(1-self.__discount/100)                        
            print("Final price of",self.name,"is",self.__price)
        else:
            print("Please input price and discount correctly")    


    # def get_price(self):
    #     return self.__price

p1 = Product()
p1.final_price()
