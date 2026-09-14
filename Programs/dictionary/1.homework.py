dict1 = {"name":"Shriyansh",
        "age":18}

dict2 = {"salary":50000,
         "phone":1234567890}

#1 to merge dictionaries

dict = {}

dict.update(dict1)
dict.update(dict2)
print(dict)

#2 to check whether key "salary" exits in dictionary

# print("salary" in dict)

#3 to check whether the key "address" does not exist

# print("key \"address\" does not exist:","address" not in dict)

#4 get function

# if("phone" in dict):
#     print(dict.get("phone"))
# else:
#     print("not found")    

