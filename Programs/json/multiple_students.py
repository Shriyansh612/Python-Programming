import json
data = []
for i in range(3):
    name = input("Enter name: ")
    age = input("enter age: ")
    marks = input("Enter marks: ")
    data.append({"name":name,"age":age,"marks":marks})

with open("test.json","w") as f:
    json_str = json.dumps(data)
    f.write(json_str)