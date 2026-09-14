numbers = [1,3,4,12,18,6,7,14]

even_numbers = list(filter(lambda n:n%2==0,numbers))

print(even_numbers)

square_even_numbers = list(map(lambda n:n**2,even_numbers))
print(square_even_numbers)

greater_than_100 = list(filter(lambda n:n>100,square_even_numbers))
print(greater_than_100)

print(sorted(greater_than_100,reverse=True))