d = {"name":"Shriyansh","age":18,"learning":"Python"}

try:
    print(d[input("Enter key: ")])
except KeyError:
    print("Key not found")    
else:
    print("Done")