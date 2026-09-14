class Product:
    class_price = {}
    class_quantity = {}
    names = []
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.class_price[self.name] = self.price
        Product.class_quantity[self.name] = self.quantity
        Product.names.append(self.name)

p1 = Product("Television", 30000,4)        
p2 = Product("Mobile Phone",25000,5)
p3 = Product("Headphones", 1500,2)
p4 = Product("Fan",2000,6)
p5 = Product("Light Bulb",500,10)

prices = sorted(Product.class_price.values())
quantities = sorted(Product.class_quantity.values())

most_expensive = ""
cheapest = ""
least_quantity = ""
highest_quantity = ""
total = 0
print(Product.names)
print(prices)
print(quantities)
print(Product.class_quantity)

for name in Product.names:
    if (Product.class_price[name]==prices[-1]):
        most_expensive = name
    if (Product.class_price[name]==prices[0]):
        cheapest = name
    if (Product.class_quantity[name]==quantities[0]):
        least_quantity = name        
    if (Product.class_quantity[name]==quantities[-1]):
        highest_quantity = name

    total += Product.class_price[name]*Product.class_quantity[name] 

print()
print("Most expensive Product:",most_expensive,Product.class_price[most_expensive])            
print("Cheapest product:",cheapest,Product.class_price[cheapest])
print("Least Quantity:",least_quantity,Product.class_quantity[least_quantity])
print("Highest Quantity:",highest_quantity,Product.class_quantity[highest_quantity])
print("Total:",total)
