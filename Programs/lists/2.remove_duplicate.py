numbers = [23,44,63,17,41,44,44,23,65,80]
filtered_numbers=[]

for i in range(len(numbers)-1,-1,-1):
    if(numbers[i]not in numbers[:i]):
        filtered_numbers.append(numbers[i])

filtered_numbers.reverse()
print(filtered_numbers)        