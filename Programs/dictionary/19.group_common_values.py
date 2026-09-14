dict1 = {
         "maths" : 78,
         "physics" : 87,
         "english" : 78,
         "hindi" : 68,
         "computer" : 87}

result = {}

for key,value in dict1.items():
    if(value not in result):
        result[value] = []

    result[value].append(key)

for key,value in result.items():
    print(key,":",*value,sep=",")

print (type(key))
print (type(value))



# {
# "a":10,
# "b":20,
# "c":30,
# "d":40
# }

# {
# "a":40,
# "b":10,
# "c":20,
# "d":30
# }

