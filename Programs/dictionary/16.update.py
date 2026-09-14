# dict1 = {"maths":88,"hindi" : 80}

# dict2 = {"hindi" : 89,
#          "biology" : 81}

# for key in dict2:
#     dict1[key] = dict2[key]

# print(dict1)    

# dict[key] = value  
# print(dict)  




student  = {}

n = int(input("how many (key-value) paris ? "))

for i in range(n):
    key = input("Enter key : ")
    value = input("Enter value : ")
    student[key] = value

print(student)



