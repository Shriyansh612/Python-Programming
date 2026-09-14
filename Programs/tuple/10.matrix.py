rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

mat = []
for i in range(rows):
    row = tuple(map(int,input().split()))
    mat.append(row)
mat = tuple(mat)

#1 to find sum of each row

# for i in range(rows):
#     print(f"Sum of row {i+1} is {sum(mat[i])}")    

#2 to find sum of each column

# for i in range(columns):
#     sum = 0
#     for j in range(rows):
#         sum+=mat[j][i]
#     print(f"Sum of column {i+1} is {sum}")  

#3 to find sum of main diagonal

# sum = 0
# for i in range(rows):
#     sum+=mat[i][i]

# print("Sum of elements of main diagonal is:",sum)      

#4 to find sum of secondary diagonal

# sum = 0
# for i in range(rows):
#     sum += mat[i][rows-i-1]

# print("Sum of elements of secondary diagonal is:",sum)  

#5 to transpose the given matrix 

# tran = []

# for i in range(columns):
#     column = ()
#     for j in range(rows):
#         column+=(mat[j][i],)
#     tran.append(column)

# tran = tuple(tran)
# print("\nTranspose:\n")
# for row in tran:
#     print(*row)