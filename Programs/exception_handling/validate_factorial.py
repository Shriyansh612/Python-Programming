try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        raise ValueError("Negative number entered")
    fact = 1
    for i in range(1,n+1):
        fact *= i 
    print(f"The factorial of {n} is {fact}")
except ValueError:
    print("Negative number is not allowed")