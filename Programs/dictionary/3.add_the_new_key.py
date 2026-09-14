student = {"name":"shriyansh",
           "age":18}
new_key = input("Enter key name: ")

if(new_key in student):
    print("Key already exists")
else:
    new_value = input("Enter value for the key: ")
    student.update({new_key:new_value})
    print(student) 
    
       