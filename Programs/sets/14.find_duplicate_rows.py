mat = [
[1,2],
[3,4],
[1,2],
[5,6]
]

duplicate = set()
A = set()

for row in mat:
    if (tuple(row) not in A):
        A.add(tuple(row))
    else:
        duplicate.add(tuple(row))  

print(duplicate)          
