import json
d={}
for i in range(3):
    key = input("Enter key name: ")
    value = input("Enter value: ")
    d[key] = value

with open("test.json","w") as f:
    json_str = json.dumps(d,indent=4)
    f.write(json_str)

