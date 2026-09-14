rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

mat = []
for i in range(rows):
    row = list(map(int,input().split()))
    if (len(row)==columns):
        mat.append(row)
    else:
        print("Input matrix correctly")
        
result = []        

for i in range(rows):
    row = []
    for j in range(columns):
        if (i==0):
            if (j==0):
                row.append(mat[1][0])
            else:
                row.append(mat[i][j-1])
        elif (i==rows-1):
            if (j==columns-1):
                row.append(mat[rows-2][columns-1])
            else:
                row.append(mat[rows-1][j+1])
        else:
            if (j==0):
                row.append(mat[i+1][j])
            elif (j==columns-1):
                row.append(mat[i-1][j])
            else:
                row.append(mat[i][j])                                                            
    result.append(row)

print("\n")

for row in result:
    print(*row)

     