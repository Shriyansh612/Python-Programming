numbers = [1,2,3,4]

condition = lambda n : n**2 if(n%2==0) else n**3

result = list(map(condition,numbers))

print(list(map(lambda n: n**2 if n%2==0 else n**3, numbers)))