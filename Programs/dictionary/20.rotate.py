dict = {
        "a":10,
        "b":20,
        "c":30,
        "d":40
        }

values = list(dict.values())
rotate = [values[-1]] + values[:-1]
# print(rotate)

result = {}
c = 0 
for key in dict:
    result.update({key:rotate[c]})
    c+=1

for key,value in result.items():
    print(key,":",value)