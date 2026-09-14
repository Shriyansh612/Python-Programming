dict = {"maths" : 90,
        "physics" : 80,
}   

temp = dict["maths"]
dict["maths"] = dict["physics"]
dict["physics"] = temp

print(dict)