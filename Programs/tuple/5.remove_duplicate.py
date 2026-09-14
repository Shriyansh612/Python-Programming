tup = tuple(map(str,input().split()))

new_tup =()
for i in range(len(tup)-1,-1,-1):
    if(tup[i] not in tup[:i]):
        new_tup+=(tup[i],)

new_tup = new_tup[::-1]
print(new_tup)