dict = {"maths":95,
        "english":90,
        "physics":88,
        "computer":92}

result = {}
keys = list(dict.keys())

for i in range(len(keys)):
    for j in range(len(keys)-i-1):
        if(dict[keys[j]]>dict[keys[j+1]]):
            keys[j],keys[j+1] = keys[j+1],keys[j]

for key in keys:
    result.update({key:dict[key]})

for key,value in result.items():
    print(key,":",value)