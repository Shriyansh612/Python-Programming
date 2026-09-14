students = (("Alice",85),("Bob",92),("Charlie",78),("David",90))

#1 To find student with highest marks

marks = tuple(map(lambda student:student[1],students))
max_marks = max(marks)
for student in students:
    if(student[1]==max_marks):
        print(f"Maximum marks {student[1]} are obtained by {student[0]}")
        break

# 2 To find student with lowest marks

min_marks = min(marks)
for student in students:
    if(student[1]==min_marks):
        print(f"Minimum marks {student[1]} are obtained by {student[0]}")

# 3 To calculate average marks

print(f"Average marks: {sum(marks)/len(marks)}")

# 4 To find students securing more than 80 marks

filtered_students = tuple(filter(lambda student:(student[0],student[1]) if student[1]>80 else None,students))
print(filtered_students)

# 5 To sort marks in descending order

students = list(students)

for i in range(len(students)):
    for j in range(len(students)-i-1):
        if(students[j][1]>students[j+1][1]):
            students[j],students[j+1] = students[j+1],students[j]

students = tuple(students[::-1])
print(students)            