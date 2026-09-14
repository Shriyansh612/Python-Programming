dict = {3 : "maths",
        2 : "physics",
        4 : "english",
        1 : "computer"}

result = {}
keys = list(dict.keys())

for i in range(len(keys)):
    for j in range(len(keys)-i-1):
        if (keys[j]>keys[j+1]):
            keys[j],keys[j+1] = keys[j+1],keys[j]

for key in keys:
    result.update({key:dict[key]})

for key,value in result.items():
    print(key,":",value)    