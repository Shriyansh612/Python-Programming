numbers = list(map(int,input().split()))

even = set(filter(lambda n:n%2==0,numbers))
odd = set(numbers) - even
print(even)
print(odd)