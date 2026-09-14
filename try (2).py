# def increment(a):
#     print(a)
#     a=a+1
#     if(a>10):
#         return a
#     else:
#         return increment(a)

# print(increment(4))    


# def determinant(mat):
#     if(len(mat)==1):
#         return mat[0][0]
#     else:
#         det = 0
#         for i in range (len(mat)):
#             temp = []
#             for m in range(1,len(mat)):
#                 row = []
#                 for n in range(len(mat)):
#                     if(m!=0 and n!=i):
#                         row.append(mat[m][n])
#                 temp.append(row)
#             det+=(-1)**(i)*mat[0][i]*determinant(temp)
#         return det

# mat = [[1]] 
# print(determinant(mat))   

# dict = {"a":10,
#         "b":20} 
         
# dict.update({"e":dict["a"]})
# dict.pop("a") 
# print(dict)    
                

# print("\n".strip()+"Hello",end="")

l1 = [1,2]
l2 = [1,2,3]

print(l1 in l2)