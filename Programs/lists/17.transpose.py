rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns"))

matrix = []
for i in range(0,rows):
    row = list(map(int,input().split()))
    matrix.append(row)

transpose = []
for i in range(columns):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)    
            
for row in transpose:
    print(*row)

# for i in range(max(rows,columns)):
#     for j in range(maxcolumns):
#         transpose[columns][rows]=matrix[rows][columns]

# for i in range(columns):
#     print(*transpose[i])
# 
# 1 2 3
# 4 5 6                    


