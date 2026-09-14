import json

with open("test.json","r") as f:
    py_obj= json.load(f)
    json_str1 = json.dumps(py_obj)
    with open("text.py","w") as f2:
        f2.write(json_str1)
    print(type(py_obj))
    with open("test1.json","w") as f1:
        json_str = json.dumps(py_obj,indent=4)
        f1.write(json_str)
    
print(json_str)
print(type(json_str))