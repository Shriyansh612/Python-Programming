keys = ["name","age","city"]
values = ["Rohit",21,"Agra"]

dict = {}
for i in range(len(keys)):
    dict.update({keys[i]:values[i]})

print(dict)    