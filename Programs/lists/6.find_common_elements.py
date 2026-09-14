A = [1,2,3,4]
B = [3,4,5,6]
common_elements =[]

for i in range(0,len(A)):
    if(A[i] in B):
        common_elements.append(A[i])

print(common_elements)        