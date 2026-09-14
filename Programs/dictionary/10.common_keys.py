dict1 = {"maths" : 60,
         "english" : 98,
         "hindi" : 87,
         "physics" : 78}
dict2 = {"maths" : 70,
         "english" : 90,
         "chemistry" : 76,
         "computer" : 88}

common_keys = []
for key in dict1:
    if(key in dict2):
        common_keys.append(key)

print(common_keys)
