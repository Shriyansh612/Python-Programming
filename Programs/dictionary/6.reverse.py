dict = {"a":1,
        "b":2,
        "c":3}

reverse = {}

for key in dict:
    reverse.update({dict[key]:key})

for key,value in reverse.items():
    print(key,":",value)