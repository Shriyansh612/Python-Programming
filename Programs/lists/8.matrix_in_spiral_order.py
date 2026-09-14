

# # 1 2 3
# # 4 5 6
# # 7 8 9

rows = int(input("Enter the number  of row : "))
cols = int(input("Enter the number  of columns : "))

matrix = []

print("Enter the matrix elements : ")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)


top =  0
bottom = rows -1
left = 0
right = cols - 1

while top <= bottom and left <= right:

    # top Row
    for i in range(left, right + 1):
        print(matrix[top][i],end=" ")
    top+=1


    #Right column
    for i in range (top, bottom + 1):
        print(matrix[i][right],end=" ")
    right -= 1

    # bottom row
    if top <= bottom:
        for i in range(right, left -1, -1):
            print(matrix[bottom][i],end=" ")
        bottom -= 1

        
    # left column
    if left <= right:
        for i in range(bottom, top-1 , -1):
            print(matrix[i][left],end=" ")
        left += 1

        



# list = [[1,2],[3,4]]
# flatten = [1, 2, 3, 4]

# result = []

# # for i in range(0,len(flatten), 2):
# #     result.append(flatten[i:i+2])

# result = [flatten[:2], flatten[2:]]

# print(result)


# flatten = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result=[]

# result = [flatten[:3],flatten[3:6],flatten[6:]]
# print(result)



# numbers = [[1,2],[3,4],[5,6]]
# flatten = []
# for i in range(0,len(numbers)):
#     for j in range(0,len(numbers[i])):
#         flatten.append(numbers[i][j])

# print(flatten)        


numbers = list(map(int,input("Enter numbers: ").split()))
target = int(input("Enter target number: "))

for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if(numbers[i]+numbers[j]==target):
            print(f"{numbers[i]}+{numbers[j]}={target}")
            break
            