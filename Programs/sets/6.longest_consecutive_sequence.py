A = set(map(int,input().split()))

longest = set()
A = set(sorted(A))

for element in A:
    temp = [element]
    for element2 in A:
        if(element2-1 == temp[-1]):
            temp.append(element2)
    if(len(temp)>len(longest)):
        longest = set(temp) 

print(longest)