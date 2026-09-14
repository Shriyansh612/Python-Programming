rows = int(input("Enter number of rows: "))

row1 = [1]
row=[]
print(1)
for i in range(2,rows+1):
    for j in range(0,i):
        if(j==0 or j==i-1):
            row.append(1)
        else:
            row.append(row1[j-1]+row1[j])
    print(*row)    
    row1 = row
    row = []            
    