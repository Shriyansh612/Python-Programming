def input_matrix():
    while True:
        print("Input a matrix: ")
        try:
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))
        except Exception as err:
            print("Row and column number must be a positive integer") 
        else:
            if (rows>0 and columns>0):
                try:
                    mat = []       
                    for i in range(rows):
                        row = list(map(float,input().split()))
                        if (len(row)==columns):
                            mat.append(row)
                        else:
                            raise 
                except Exception as err:
                    print("Invalid matrix") 
                else:
                    return mat
            else:
                print("Row and column number must be a positive integer")                

def print_matrix(mat):
    print()
    for i in range(len(mat)):
        print(*mat[i])

def order(mat):
    return str(len(mat))+"x"+str(len(mat[0]))

def transpose(mat):
    trans = []
    for i in range(int(order(mat)[2])):
        row = []
        for j in range(int(order(mat)[0])):
            row.append(mat[j][i])
        trans.append(row)
    return trans

def square_matrix(mat):
    if (order(mat)[0]==order(mat)[2]):
        return True
    else:
        return False

def determinant(mat):
    if (square_matrix(mat)==True):
        det = 0
        if (int(order(mat)[0])==1):
            return mat[0][0]
        else:
            for i in range(0,int(order(mat)[0])):
                temp = []
                for a in range(1,int(order(mat)[0])):
                    row = []
                    for b in range(0,int(order(mat)[0])):
                        if (b!=i):
                            row.append(mat[a][b])
                    temp.append(row)
                det += mat[0][i]*(-1)**(i)*determinant(temp)
            return det                
    else:
        return

def add(mat1,mat2):
    if (order(mat1)!=order(mat2)):
        print("Addition/Subtraction can be performed only on the matrices of same order")
        return mat1     
    else:
        result = []
        for i in range(int(order(mat1)[0])):
            row = []
            for j in range(int(order(mat1)[2])):
                row.append(mat1[i][j]+mat2[i][j])
            result.append(row)
        return result
    
def subtract(mat1,mat2):
    return add(mat1,scalar_mult(mat2,-1))

def scalar_mult(mat,k):
    for i in range(int(order(mat)[0])):
        for j in range(int(order(mat)[2])):
            mat[i][j] = k*mat[i][j]
    return mat

def multiplication(mat1,mat2):
    if (order(mat1)[2]!=order(mat2)[0]):
        print("Multiplication can't be performed")
        return
    else:
        result = []
        for i in range(int(order(mat1)[0])):
            row = []
            for j in range(int(order(mat2)[2])):
                sum = 0
                for r in range(int(order(mat1)[2])):
                    sum += mat1[i][r]*mat2[r][j]
                row.append(sum)
            result.append(row)        
        return result    



mat1 = input_matrix()              
mat2 = input_matrix()              
print(multiplication(mat1,mat2))

