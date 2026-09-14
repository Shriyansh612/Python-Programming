students_marks = [["Mohan",56],["Rahul",78],["Varun",30]]

filtered = list(filter(lambda student:student[1]>=33,students_marks))
print(filtered)

result = list(map(lambda student:[student[0],student[1]+5],filtered))
print(result)