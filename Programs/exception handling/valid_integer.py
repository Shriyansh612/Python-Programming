while True:
    try:
        n = int(input("Enter integer: "))
    except ValueError:
        print("Please input interger")
    else:
        print("Your number is:",n)
        break        