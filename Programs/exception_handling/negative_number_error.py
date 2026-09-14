try:
    n = int(input("Enter a non negative number: "))
    if (n<0):
        raise NegativeNumberError
    print(n)
except ValueError:
    print("Enter an integer")  
except Exception as NegativeNumberError:
    print("Negative number is not allowed")          