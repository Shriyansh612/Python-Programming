import json
names = ["Shriyansh","Raghu","Jatin","Ravi","Priyanshu"]
with open("test.json","w") as f:
    json_str = json.dumps(names)
    f.write(json_str)
    print(type(json_str))