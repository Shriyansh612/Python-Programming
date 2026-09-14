try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print("Division:",a/b)
except ValueError:
    print("Please enter valid integer")    
except ZeroDivisionError:
    print("Division by 0 is not possible")    