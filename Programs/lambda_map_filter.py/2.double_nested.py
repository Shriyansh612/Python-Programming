numbers = [[1,2],[3,4]]

result = list(map(lambda row:list(map(lambda n:n*2,row)),numbers))

print(result)