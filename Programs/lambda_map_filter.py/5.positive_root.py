numbers = [1,4,9,0,-9,-1]

print(list(map(lambda n : n**(0.5),list(filter(lambda n:n>0,numbers)))))