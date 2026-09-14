dict = {"maths" : 40,
        "english" : 70,
        "physics" : 50}

key = input("Enter key to be deleted: ")
if (key in dict):
    del dict[key]
    print(dict)
else:
    print("Key not found")    