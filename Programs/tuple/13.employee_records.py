employees = ((101,"Alice",50000),
             (102,"Bob",75000),
             (103,"Charlie",60000),
             (104,"David",90000),
             (105,"Eva",70000))

#1 to find employee with highest salary

# salary = tuple(map(lambda employee : employee[2],employees))
# max_index = salary.index(max(salary))
# print(f"{employees[max_index][1]} has the highest salary of {employees[max_index][2]}")

#2 to find employee with lowest salary

# salary = tuple(map(lambda employee : employee[2],employees))
# min_index = salary.index(min(salary))
# print(f"{employees[min_index][1]} has the lowest salary of {employees[min_index][2]}")

#3
salary = tuple(map(lambda employee : employee[2],employees))
# average_salary = sum(salary)/len(salary)
# print("Average salary of employees:",average_salary)

#4 to print employees having salary higher than average

# print(tuple(filter(lambda employee : (employee[1],employee[2]) if  employee[2]>average_salary else None,employees)))

#5 to print employees having salary lower than average

# print(tuple(filter(lambda employee : (employee[1],employee[2]) if  employee[2]<average_salary else None,employees)))

#6 search by id

# id = int(input("Enter id: "))
# check = 0

# for i in range(len(employees)):
#     if (employees[i][0]==id):
#         check = 1
#         print("Employee found:",employees[i])
#         break

# if(check==0):
#     print("Employee not found")   


     