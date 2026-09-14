chance = 0
username = "Shriyansh"
password = "12345678"
try:
    username1 = input("Enter username: ")
    if (username!=username1):
        print("Incorrect username")
    else:
        for i in range(3):
            password1 = input("Enter password: ")
            if (password!=password1):
                print("Incorrect password")
                chance+=1
                if (chance==3):
                    raise
            else:
                print("Correct password")
                break
except Exception as err:
    print("Maximum attempts done")                     