# mat1 = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# mat2 = [[0,1,2],
#         [3,4,5],
#         [6,7,8]]

def mat3x3_input():     #function to input 3x3 matrix
    mat = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    for i in range (0,3):
        for j in range(0,3):
            mat[i][j]=int(input())
    print()            
    for i in range (0,3):
        for j in range (0,3):
            print(mat[i][j],end=" ")
        print()
    print()                
    return mat 

mat1 = mat3x3_input()        
mat2 = mat3x3_input()        

mat3 = [[0,0,0],
        [0,0,0],
        [0,0,0]]

print("Sum of two matrices are: ")

for i in range (0,3):
    for j in range (0,3):
        mat3[i][j] = mat1[i][j] + mat2[i][j]
        print(mat3[i][j], end=" ")
    print()        
