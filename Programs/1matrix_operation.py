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

mat1, order1, nature1 = matrix_input() 

def trace():
    if(nature1==True):
        if (order1[0]==order1[2]):
            print("Trace of the given matrix is:")
            trace = 0
            for i in range(0,int(order1[0])):
                trace += mat1[i][i]
            print(trace)
        else:
            print("Trace is only defined for square matrices")        

def minor():
    if (nature1==True):
        if (order1[0]==order1[2]):
                        