class Product:
    # def __init__(self):
    #     self.products = [{"phone":25000,"keyboard":1500,"mouse":500,"tv":30000,"pc":60000,"laptop":80000,"headphones":1200,
    #                     "shirt":500,"jeans":700,"shorts":300,"shoes":1500,"t-shirt":400,
    #                     "mathematics":600,"physics":500,"chemistry":400,"english":450,"programming":700}]
    def display(self):
        pass
    def calculate_bill(self):
        pass

class Electronics(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        gst = self.price * 0.18
        return self.price + gst

    def display(self):
        print("Product:",self.name)                                                
        print("Price:",self.price)

class Clothing(Product):
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def calculate_price(self):
        discount = self.price*0.2
        return self.price-discount

    def display(self):
        print("Product:",self.name)                        
        print("Price:",self.price)

class Book(Product):
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def calculate_price(self):
        discount = 50
        return self.price - discount

    def display(self):
        print("Product:",self.name)                        
        print("Price:",self.price)

# inputs 

electronics_name = input("Enter electronics name : ")
electronics_price = float(input("Enter electronics price :  "))

clothing_name = input("Enter clothing name : ")
clothing_price = float(input("Enter clothing price :  "))

book_name = input("Enter book name : ")
book_price = float(input("Enter book price :  "))

# Objects
products = [
    Electronics(electronics_name, electronics_price),
    Clothing(clothing_name, clothing_price),
    Book(book_name,book_price)
]

# polymorphism

for product in products:
    product.display()
    print("Final price : ", product.calculate_price())
    print()





# Sword     → Sword attack!
# Bow       → Arrow fired!
# MagicWand → Magic spell!
# Shield    → Shield activated!