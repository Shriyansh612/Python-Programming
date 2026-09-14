# n = int(input("Enter  : "))

# number =  []

# for i in range(n):
#     value = int(input("enter the element: "))
#     number.append(value)

# print("list = ", number)


rows = int(input("Enter number of rows : "))
columns = int(input("enter number of column : "))

matrix = []
valid = True

for i in range(rows):
    data = input(f"Enter row {i+1}: ").split()

    if len(data) != columns:
        print('Please fill all data.')
        valid =  False
        break

    row = []

    for j in range(columns):
        row.append(int(data[j]))

    matrix.append(row)

if (valid):
    print("\nMatrix: ")
    for i in range(rows):
        for j in range(columns):
            print(matrix[i][j], end=" ")

        print()