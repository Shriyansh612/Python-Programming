def input_matrix():     #function to input a matrix
    print("Input a matrix: ")
    m = input("Enter number of rows: ").strip()     #to input number of rows
    if (m.isdigit()):
        if(int(m)>0):
            n = input("Enter number of columns: ").strip()      #to input number of columns
            if(n.isdigit()):
                if(int(n)>0):
                    matrix = []
                    for i in range(int(m)):     #rows
                        row = []
                        try:
                            row = list(map(float,(input().strip()).split()))
                            if(len(row)==n):
                                pass
                        except:
                            print("Please input matrix entries correctly")
                            input_matrix()
                        matrix.append(row)
                    return matrix                               

                                      
                        # row = input().split()
                        # if(len(row)!=int(n)):
                        #     print("Please fill all entries")
                        #     c=1
                        #     break
                        # for element in row:
                            # if(element.isdigit() == False):
                            #     c=1
                            #     print("Please enter only integer input")
                            #     break
                        # if (c==1):
                        #     break    
                        # row = list(map(int,row))

                        # matrix.append(row)
                    # if(c==1):
                    #     return None,False
                    # else:
                    #     return matrix,True
                else:
                    print("Number of columns must be a positive integer")
                    input_matrix()
            else:
                print("Number of columns must be a positive integer")
                input_matrix()        
        else:
            print("Number of rows must be a positive integer")
            input_matrix()                   
    else:
        print("Number of rows must be a positive integer")
        input_matrix()                        


def print_matrix(mat):      #function to print a matrix
    print("Result: ")
    for row in mat:
        print(*row)

def order(mat):         #function to determine the order of a given matrix
    return str(len(mat))+"x"+str(len(mat[0]))

def addition(mat1,mat2):        #function to add two matrices
    if(order(mat1)==order(mat2)):
        result = []
        for i in range(int(order(mat1)[0])):
            row = []
            for j in range(int(order(mat1)[2])):
                row.append(mat1[i][j]+mat2[i][j])
            result.append(row)

        print_matrix(result)
        return result
    else:
        print("Addition can be performed only on matrices of same order")
        return mat1

def subtraction(mat1,mat2):         #function to subtract two given matrices
    if(order(mat1)==order(mat2)):
        result = []
        for i in range(int(order(mat1)[0])):
            row = []
            for j in range(int(order(mat1)[2])):
                row.append(mat1[i][j]-mat2[i][j])
            result.append(row)

        print_matrix(result)
        return result
    else:
        print("Subtraction can be performed only on matrices of same order")
        return mat1

def check_square_matrix(mat):       #function to check whether a given matrix is a square matrix or not
    if(order(mat)[0]==order(mat)[2]):
        return True
    else:
        return False

def transpose(mat):         #function to transpose a given matrix
    tran = []
    for i in range(int(order(mat)[2])):
        row = []
        for j in range(int(order(mat)[0])):
            row.append(mat[j][i])
        tran.append(row)

    print_matrix(tran)
    return tran

def scalar_multiplication(mat):     #to multiply the given matrix by a scalar
    k = input("Enter scalar to be multiplied with: ")
    k = k.strip()
    if((k[0]=="-" and k[1:].isdigit()) or k.isdigit()):
        result = []
        k = int(k)
        for row in mat:
            result.append(list(map(lambda n:n*k,row)))
        print_matrix(result)
        return result
    else:
        print("Enter valid scalar multiplier")
        return mat    
    
def rotate_clock(mat):      #to rotate a matrix clockwise
    result = []
    for i in range(int(order(mat)[2])):
        row = []
        for j in range(int(order(mat)[0])):
            row.append(mat[int(order(mat)[0])-j-1][i]) 
        result.append(row)
    print_matrix(result)
    return result 

def rotate_anti_clock(mat):     #to rotate a matrix anticlockwise
    result = []
    for i in range(int(order(mat)[2])):
        row = []
        for j in range(int(order(mat)[0])):
            row.append(mat[j][int(order(mat)[2])-1-i])
        result.append(row)
    print_matrix(result)
    return result 

def trace(mat):         #to determine the trace of a matrix
    if(check_square_matrix(mat)):
        tr = 0
        for i in range(0,int(order(mat)[0])):
            tr+=mat[i][i]
        print("Trace of the given matrix:",tr) 
    else:
        print("Trace can only be determined for square matrix only")  

def determinant(mat):       #to find determinant of a matrix
    if(check_square_matrix(mat)):
        if(len(mat)==1):
            return mat[0][0]
        else:
            det = 0
            for i in range (len(mat)):
                temp = []
                for m in range(1,len(mat)):
                    row = []
                    for n in range(len(mat)):
                        if(m!=0 and n!=i):
                            row.append(mat[m][n])
                    temp.append(row)
                det+=(-1)**(i)*mat[0][i]*determinant(temp)
            return det
    else:
        print("determinant is only defined for square matrices")                                          

mat1 = input_matrix() 
nat1 = True
if(nat1):
    print('''
Choose Operation:
          0. To End
          1. Order
          2. Transpose
          3. Check for square matrix
          4. Addition
          5. Subtraction
          6. Scalar Multiplication
          7. Rotate Clockwise
          8. Rotate AntiClockwise
          9. Trace
          10. Determinant
          11. To input new matrix

''')
    op = -1
    while(op!=0):
        op = input("Enter operation: ")
        if(op.isdigit()):
            if(int(op)<12):
                op = int(op)
                match op:
                    case 0:
                        print("Thank you for using program")
                    case 1:
                        print("Order of given matrix is:",order(mat1))
                    case 2:
                         mat1 = transpose(mat1)
                    case 3:
                        if(check_square_matrix(mat1)):
                            print("It is a square matrix")
                        else:
                            print("It is not a square matrix")
                    case 4:
                        mat2, nat2 = input_matrix()
                        if(nat2):
                            mat1 = addition(mat1,mat2)
                    case 5:
                        mat2, nat2 = input_matrix()
                        if(nat2):
                            mat1 = subtraction(mat1,mat2)
                    case 6:
                        mat1 = scalar_multiplication(mat1) 
                    case 7:
                        mat1 = rotate_clock(mat1)
                    case 8:
                        mat1 = rotate_anti_clock(mat1)
                    case 9:
                        trace(mat1) 
                    case 10:
                            print("Determinant of the given matrix: ",determinant(mat1)) 
                    case 11:
                        mat1 = input_matrix()                                                                 
            else:
                print("Please enter valid input")
        else:
            print("Please enter valid input")                


    