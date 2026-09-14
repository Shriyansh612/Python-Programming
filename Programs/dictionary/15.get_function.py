dict = {"maths":88,
        "physics":76,
        "chemistry":85,
        "english":79}

key = input("Enter key: ")

if(key not in dict):
    print(None)
else:
    print(key,":",dict[key])    