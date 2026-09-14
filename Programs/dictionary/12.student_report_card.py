students = {"ravi" : 95,
            "raju" : 32,
            "ram" : 77,
            "raghav" : 29,
            "vaibhav" : 65}

highest_marks = max(students.values())
lowest_marks = min(students.values())
average = sum(students.values())/len(students)

pass_students = {}
fail_students = {}

for key in students:
    if(students[key]==highest_marks):
        print("Highest marks scored by:",key,":",students[key])
    if(students[key]==lowest_marks):
        print("Lowest marks scored by:",key,":",students[key])
    if(students[key]>=33):
        pass_students.update({key:students[key]})
    else:
        fail_students.update({key:students[key]})

print("Average Marks:",average)
print("Passed students:",pass_students)
print("Failed students:",fail_students)
