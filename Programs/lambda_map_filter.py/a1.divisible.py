numbers = [15,18,30,35,80]
filtered_numbers = list(filter(lambda n:n%15==0,numbers))
print(filtered_numbers)

print(list(map(lambda n:n*n,filtered_numbers)))