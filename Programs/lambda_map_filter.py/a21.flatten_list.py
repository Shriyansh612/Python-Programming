numbers = [[1,2],[3,4]]
flatten = []

for i in range(0,2):
    flatten.extend(numbers[i])

print(flatten)

print(list(filter(lambda n:n%2==0,flatten)))    