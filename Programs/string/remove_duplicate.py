text = input("Enter a string: ")
result = ""

for char in text :
    if char not in result:
            result+=char
          
print("string after removing is : ", result)     