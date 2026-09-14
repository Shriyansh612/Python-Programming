password = input("Enter your password: ")
if (len(password)<8):
    raise ValueError("Password must be atleast 8 characters long")
else:
    print("Password accepted")