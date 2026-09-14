tup = ((1,2,3),(4,5,6),(7,8,9))

flatten = ()
for i in range(len(tup)):
    for j in range(len(tup[i])):
        flatten += (tup[i][j],)

print(*flatten)        