import json

 
students = {}

for i in range(3):

    student_id = input("Enter studnet id : ")
    name = input("Enter the anme  : ")
    age = int(input("Enter age : "))
    city = input("Enter city : ")
    
    math = int(input("Enter math marks  : "))
    science = int(input("Enter secience marks  : "))
    english = int(input("Enter english marks  : "))

    skill1  = input("enter skill 1 :")
    skill2  = input("enter skill 2 :")

    total = math +  science + english
    percentage =  total / 3*100

    students[student_id] = {
        "name"  : name,
        "age" : age,
        "city" : city,

        "marks" : {
            "math" : math,
            "science" : science,
            "english" : english,
        },

        "skills" : [ skill1, skill2 ],

        
        "total" : total,
        "percentage" : percentage

    }


    json_str= json.dumps(students, indent=4)

    with open("test.json","w") as f:
        f.write(json_str)


print("Data saved successfully")

print(json_str)
