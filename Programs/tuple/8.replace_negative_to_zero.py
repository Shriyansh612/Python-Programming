tup = tuple(map(int,input().split()))

result = tuple(map(lambda n:n if n>0 else 0,tup))

print(result)