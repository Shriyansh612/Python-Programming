dict = {"name":"shriyansh",
        "user":"shriyansh",
        "subject":"python",
        "learning":"python"}
# print(dict.values())

result = {}

for key,value in dict.items():
    if value not in result.values():
        result.update({key:value})

for index,(key,value) in enumerate(result.items()):
    print(f"{index} = {key} : {value}")