import json
dict = {"name":"Shriyansh","age":19,"city":"agra"}
with open("test.json","w") as f:
    json_str = json.dumps(dict)
    f.write(json_str)
