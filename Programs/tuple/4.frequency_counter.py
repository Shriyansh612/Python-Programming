tup = tuple(map(str,input().split()))

for i in range(len(tup)):
    freq = 0
    for j in range(i,len(tup)):
        if(tup[i]==tup[j] and (tup[i] not in tup[:i])):
            freq+=1
    if(freq>0):            
        print(f"Frequency of {tup[i]} is: {freq}")            