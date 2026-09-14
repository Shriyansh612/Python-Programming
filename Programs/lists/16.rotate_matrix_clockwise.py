order = int(input("Enter order of matrix: "))
matrix = []

for i in range(order):
    row = list(map(int,input().split()))
    matrix.append(row)

result = []


for i in range(order):
    row2 = []
    for j in range(order):
        row2.append(0)
    result.append(row2)    

for i in range(order):
    for j in range(order):
        result[j][order -1 -i] = matrix[i][j]
       
        
print("Rotated matrix : ")    

for row in result:
    print(*row)

result[i][j]=matrix[j][i]    


1 2 3
4 5 6
7 8 9

transpose

1 4 7
2 5 8
3 6 9

clock

7 4 1
8 5 2
9 6 3

anti 

3 6 9
2 5 8
1 4 7
