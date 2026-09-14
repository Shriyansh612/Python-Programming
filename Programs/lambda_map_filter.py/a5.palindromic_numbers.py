numbers = [121,33,5,43,12]

print(list(filter(lambda n:n if(n==int(str(n)[::-1])) else None,numbers)))