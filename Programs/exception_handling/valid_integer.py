while True:
    try:
        n = int(input("Enter an integer: "))
        print(n)
        break
    except ValueError:
        print("Enter a valid integer")
