# mat1 = [[1]]
# mat2 = [[1,2],[3,4]]

def minor1(temp1):
    return temp1[0][0]

# minor1(mat1)    

def minor2(temp2):
    for i in range(0,2):
        for j in range(0,2):
            temp3 = [[0]]
            for m in range(0,2):
                for n in range(0,2):
                    if(m!=i and n!=j):
                        temp3[0][0] = temp2[m][n]
            print(f"Minor of({i},{j}): {minor1(temp3)}")     

# minor2(mat2) 


# def minor3(temp4):
#     for i in range(0,3):
#         for j in range(0,3):
#             temp5=[[0,0],[0,0]]
            
# def det2(temp):
#     det = temp[0][0]*temp[1][1]-temp[0][1]*temp[1][0]
#     return det

def cofactor2_element(temp,index1,index2):
    cofactor = None
    for i in range(0,2):
        for j in range(0,2):
            if (i!=index1 and j!=index2):
                cofactor = ((-1)**(i+j))*temp[i][j]
    return cofactor

def det2(temp):
    det = 0
    for i in range(0,2):
        det = det+temp[0][i]*cofactor2_element(temp,0,i)
    return det


# def input_mat_2():
#     print("Enter elements of 2x2 matrix: \n")
#     temp=[[0,0],[0,0]]
#     for i in range(0,2):
#         for j in range(0,2):
#             temp[i][j]=int(input())
#     print("\n")            
#     for i in range(0,2):
#         for j in range(0,2):
#             print(temp[i][j],end=" ")
#         print()            
#     print("\n")
#     return temp


# print(det2(input_mat_2()))                    


def cofactor3_element(temp,index1,index2):
    temp2 = [[0,0],[0,0]]
    c,d=0,0
    for i in range(0,3):
        for j in range(0,3):
            if (i!=index1 and j!=index2):
                temp2[c][d] = temp[i][j]
                if(d==1):
                    c=1
                d=1
    cofactor = (-1)**(index1+index2)*det2(temp2)
    return cofactor


def det3(temp):
    det = 0
    for i in range(0,3):
        det = det + temp[0][i]*cofactor3_element(temp,0,i)        
    return det    

# def input_mat_3():
#     print("Enter elements of 3x3 matrix: \n")
#     temp=[[0,0,0],[0,0,0],[0,0,0]]
#     for i in range(0,3):
#         for j in range(0,3):
#             temp[i][j]=int(input())
#     print("The entered matrix is:\n")            
#     for i in range(0,3):
#         for j in range(0,3):
#             print(temp[i][j],end=" ")
#         print()            
#     print("\n")
#     return temp

print("Determinant of the given matrix is:", det3(input_mat_3()))        

# def input_mat_4():
#     print("Enter elements of 3x3 matrix: \n")
#     temp=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#     for i in range(0,4):
#         for j in range(0,4):
#             temp[i][j]=int(input())
#     print("The entered matrix is:\n")            
#     for i in range(0,4):
#         for j in range(0,4):
#             print(temp[i][j],end=" ")
#         print()            
#     print("\n")
#     return temp

def cofactor4_element(temp,index1,index2):
    temp2 = [[0,0,0],[0,0,0],[0,0,0]]
    c=d=0
    for i in range(0,4):
        for j in range(0,4):
            if (i!=index1 and j!=index2):
                temp2[c][d]=temp[i][j]
                if(d==2 and c==0):
                    c==1


