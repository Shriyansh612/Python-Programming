import json
students = []
for i in range(5):
    roll_no = int(input("Enter your roll no.: "))
    name  = input("Enter your name: ")
    age = input("Enter your age: ")
    marks = int(input("enter your marks: "))
    students.append({"roll_no":roll_no,"name":name, "age":age, "marks":marks})

for i in range(4):
    for j in range(5-i-1):
        if (students[j]["marks"]>students[j+1]["marks"]):
            students[j],students[j+1] = students[j+1],students[j]

with open("test1.json","w") as f:
    json_str = json.dumps(students)
    f.write(json_str)