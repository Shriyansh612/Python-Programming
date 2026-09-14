email = input("Enter your email: ")
try:
    if (email != email.lower()):
        print(1)
        raise
    if (" " in email):
        print(2)
        raise
    if (email[0].isalpha()==False):
        print(3)
        raise
    if (email.count("@")!=1):
        print(4)
        raise
    if (email[-4:]!=".com" and email[-4:]!=".org" and email[-3:]!=".in"):
        print(5)
        raise
    print("Correct email")
except Exception as err:
    print("Enter a valid email")