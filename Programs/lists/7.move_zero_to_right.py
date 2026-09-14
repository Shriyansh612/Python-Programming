numbers = [0,1,0,3,12]

for i in range(0,numbers.count(0)):
    numbers.remove(0)
    numbers.append(0)

print(numbers)    