# class User:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

# class Customer(User):
#     def __init__(self,name,id,coupon):
#         super().__init__(name,id)
#         self.coupon = coupon
#         self.cart = []
#         self.prices = []
#         # self.quantities = []
#         self.discount_percent = 0

#     def add_to_cart(self):
#         item = " "
#         price = 0
#         # quantity = 0
#         print("Enter products") 
#         print("To stop entering type \"stop\"")       
#         while (item!="stop"):
#             item = input("Enter product name: ")
#             price = int(input("Enter price: "))
#             self.cart.append(item)
#             self.prices.append(price)                
#         print("\nCart:",*self.cart,"\n")

#     def remove_products(self):
#         print("Enter products to remove: ")
#         print("Type \"stop\" when you are done")
#         item = ""
#         while (item!="stop"):
#             item = input("Enter product name: ")
#             if (item in self.cart):
#                 self.cart.remove(item)
#             else:
#                 print("Entered item is not in cart")    

#     def total_price(self):
#         return sum(self.prices)

#     def discounted(self):
#         if (self.coupon):
#             if (self.total_price()<=1000):
#                 self.discount_percent = 2
#             elif (self.total_price()<=2000):
#                 self.discount_percent = 5
#             elif (self.total_price()<=5000):
#                 self.discount_percent = 10
#             else:
#                 self.discount_percent = 20
#         return self.total_price()*(1-self.discount_percent/100)

#     def place_order(self):
#         print("Placing Order...")   
#         self.add_to_cart()                                 
#         self.remove_products()
#         if (self.cart!=None):
#             print("Order placed")
#             self.cart = []
#             self.prices = []
#             print("Total Price:",self.total_price())
#             print("Final Price:",self.discounted())
#         else:
#             print("Order can't be placed as cart is empty")    

            
# c1 = Customer("Shriyansh",101,True)
# c1.place_order()




class User:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Customer(User):
    def __init__(self):
        name = input("Enter your name: ")
        id = input("Enter your customer id: ")
        super().__init__(name,id)
        self.coupon = False
        self.cart = {}       
        # self.prices = []

    def add_to_cart(self):
        item = input("Enter product name: ")
        price = int(input("Enter price: "))
        self.cart[item] = price

    def remove_from_cart(self):
        item = input("Enter product to remove from cart: ")
        if (item in self.cart):
            del self.cart[item]
        else:
            print("Given item is not in cart")

    def show_cart(self):
        print("\nCart..\n")
        if (self.cart == {}):
            print("\nCart is empty\n")
        else:
            for item in self.cart:                        
                print(item,":",self.cart[item])
        print("\nTotal Price: ",sum(self.cart.values()))
        
    def apply_coupon(self):
        self.coupon = input("Enter coupon(True or False): ")
        if (self.coupon=="True"):
            print ("Coupon of 20 percent is  applied")
            self.coupon = True
        else:
            print("Invalid Coupon")            
            self.coupon = False

    def place_order(self):
        if (self.coupon):
            print("\nOrder Placed")
            print("\nBill\n")
            print("Total price:",sum(self.cart.values()))
            print("Discounted Price:",sum(self.cart.values())*0.8)
            print("Discount:",sum(self.cart.values())*0.2)
            self.cart = {}

        else:
            print("\nBill\n")
            print("Total price:",sum(self.cart.values()))

s1 = Customer()
print('''Welcome to Shopping Cart..''')      

while(True):
    print('''

1 to Add product to Cart
2 to Remove product to Cart
3 to Show Cart
4 to Apply Coupon
5 to Place Order
6 to Exit
    ''')
    operation = 0
    operation = int(input())
    match operation: 
        case 1: 
            s1.add_to_cart()
        case 2:
            s1.remove_from_cart()
        case 3:
            s1.show_cart()                        
        case 4: 
            s1.apply_coupon()            
        case 5:
            s1.place_order()    
        case 6:
            print("Thank You for Shopping")
            break            


  

    