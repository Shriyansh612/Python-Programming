def mat_input():
    mat = []
    rows = int(input("Enter number of rows: "))
    for i in range(rows):
        row = list(map(int,input().split()))
        mat.append(row)
    return mat

a = mat_input()        
b = mat_input()        
print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j]+b[i][j],end = " ")
    print()    
