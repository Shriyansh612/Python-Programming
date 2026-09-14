# numbers = [1,2,3,4,5]

# even = list(filter(lambda n:n%2==0,numbers))

# odd = list(filter(lambda n:n%2!=0,numbers))

# print("Even numbers:",even)
# print("Odd numbers:",odd)


A=[1,2,3]
B =[4,5,6]
merge = []

for i in range(0,len(A)):
    merge.append(A[i])
    merge.append(B[i])

print(merge)    


