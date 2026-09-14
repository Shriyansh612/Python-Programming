d1 = {"a" : 10,
      "b" : 20,
      "c" : 30}
d2 = {"b" : 20,
      "c" : 40,
      "d" : 50}

common_key_value = {}

for key in d1:
    if(key in d2):
        if(d1[key]==d2[key]):
            common_key_value.update({key:d1[key]})

print(common_key_value)            