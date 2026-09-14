def matrix_input():     #function to input 2 matrices of any order less than 4x4

    m=input("Enter number of rows: ")   #Number of rows
    if(m.isdigit()):        #To check if rows is digit not alphabet
        if (int(m)==0): #To check if rows are non zero
            print("Number of rows cannot be zero")
            return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],"nil",False    #Return false so that the other functions do not run
        elif (int(m)>4):    #Applying limit of matrix size to be atmost 4x4
            print("Number of rows must be less than 5")
            return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],"nil",False    #Return false so that the other functions do not run     
        else:
            n = input("Enter number of columns: ")  #Number of columns
            if (n.isdigit()):   #Same as rows
                if(int(n)==0):
                    print("Number of columns cannot be zero")
                    return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],"nil",False
                elif(int(n)>4):
                    print("Number of columns must be less than 5")
                    return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],"nil",False    
                else:       #When both rows and column number are correctly inputed
                    mat = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]     #default matrix
                    for i in range (0,int(m)):      #To input rows
                        for j in range (0,int(n)):  #To input columns
                            mat[i][j]=int(input())  #Inputing values for matrix
                    print()

                    #To display the inputed matrix
                    for i in range(0,int(m)):
                        for j in range(0,int(n)):
                            print(mat[i][j],end=" ")
                        print()

                    print()
                    order = m+"x"+n     #To display order of inputed matrix
                    print("Order:",order)
                    print()
                    return mat, order, True     #Returns the matrix, its order and true so that other functions could run                                   

            else:
                print("Number of columns should be a positive integer")     #Barrier on columns
                return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],"nil",False            
    else:
        print("number of rows should be a positive integer")    #Barrier on rows
        return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],"nil",False  

# mat1,order1,nature1 = matrix_input()    #making first matrix                    
# mat2,order2,nature2 = matrix_input()    #making second matrix

# def matrice_add():      #function to add two inputed matrices 
#     if(nature1==True and nature2==True):    #to make sure that function doesnot run even if the entered matrices are invalid
#         if (order1!=order2):    #for addition matrices must have same order
#             print("Matrix Addition is only possible with matrices of same order")
#         else:       #when matrices are of same order
#             m=order1[0]     #rows
#             n=order2[2]     #columns
#             print()
#             print("The sum of the two matrices is: ")
#             for i in range(0,int(m)):   #for rows
#                 for j in range(0,int(n)):   #for columns
#                     print(mat1[i][j]+mat2[i][j],end=" ")    #adding corresponding elements of matrices and displaying them
#                 print()                

# def matrice_multiplication():       #function to multiply to given matrices
#     if (nature1==True and nature2==True):   #to make sure that function doesnot run even if the entered matrices are invalid
#         if(order1[2]==order2[0]):   #Condition for matrix multiplication: Number of columns in first matrix must be equal to the number of rows in second matrix
#             print("Multiplication")
#             order3 = order1[0]+"x"+order2[2]    #Order of the resultant matrix after multiplication
#             print("Order of resultant matrix is:",order3)
#             sum = 0     #this refers to each element of the resultant matrix which is sum of multiplication of row by columns
#             print("Resultant Matrix: ")
#             for i in range(0,int(order3[0])):   #for rows
#                 for j in range(0,int(order3[2])):   #for columns
#                     for k in range(0,int(order1[2])):   #(i,j)th element of resultant matrix = summation(A(i,k)*B(k,j)) where k is the number of columns in 1st matrix or number of rows in 2nd matrix which are equal
#                         sum = sum+mat1[i][k]*mat2[k][j] #calculating elements of resultant matrix
#                     print(sum,end=" ")
#                     sum=0   #default value
#                 print()
#         else:   #executes when multiplication is not defined
#             print("Multiplication is not defined for given matrices\nas for multiplication number of columns in first matrix\nmust be equal to the number of rows in the second matrix")           

# matrice_add()
# matrice_multiplication()

# def matrice_subtraction():      #function to add two inputed matrices 
#     if(nature1==True and nature2==True):    #to make sure that function doesnot run even if the entered matrices are invalid
#         if (order1!=order2):    #for addition matrices must have same order
#             print("Matrix Addition is only possible with matrices of same order")
#         else:       #when matrices are of same order
#             m=order1[0]     #rows
#             n=order2[2]     #columns
#             print()
#             print("The sum of the two matrices is: ")
#             for i in range(0,int(m)):   #for rows
#                 for j in range(0,int(n)):   #for columns
#                     print(mat1[i][j]-mat2[i][j],end=" ")    #adding corresponding elements of matrices and displaying them
#                 print()
# m=input("Enter number of rows: ")           
# n = input("Enter number of columns: ")

# def test():

#     mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]]

#     for i in range(int(m)):
#         row = input(f"enter row {i+1}: ").split()

#         if len(row) != int(n):
#             print("invalid number of elements.")
#             return [[0, 0, 0, 0], [0, 0, 0, 0], [0,0, 0, 0],[0, 0, 0, 0]], "nil", false

#         for j in range (int(n)):
#             mat[i][j] = int(row[j])


#     for i in range(0,int(m)):
#         for j in range(0, int(n)):
#             print(mat[i][j], end=" ")
#         print()

        
# test()            