products = [
    ["Laptop", 50000],
    ["Mouse", 800],
    ["Keyboard", 1500],
    ["Monitor", 12000],
    ["Pen", 50]
]

filtered_products = list(filter(lambda product:product[1]>1000, products))
print(filtered_products)

print(list(map(lambda product:[product[0],product[1]*1.18],filtered_products)))