try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Age must be an integer")
else:
    print("Your age is:",age)    