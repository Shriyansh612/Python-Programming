#flatten
# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))

# numbers =[]
# for i in range(0,rows):
#     row = list(map(int,input().split()))
#     numbers.append(row)

# flatten = []

# for i in range(0,rows):
#     flatten.extend(list(map(lambda n:n,numbers[i])))

# print(flatten)    

#deflatten

numbers = list(map(int,input().split()))

# [1,2,3,4]==>[[1,2],[3,4]]

deflatten = []
for i in range(0,len(numbers),2):
    deflatten.append(numbers[i:i+2])

print(deflatten)    