#LIS = Longest Increasing Subsequence


tuple = (50, 3, 10, 7, 40, 80)

longest = ()

for i in range(len(tuple)):
    temp = (tuple[i],)   # current increasing sequence
    last = tuple[i]     # seques last element ko store
    for j in range(i + 1,len(tuple)):
        if tuple[j] > last:
            temp+=(tuple[j],)1
            last = tuple[j]

    if(len(temp) > len(longest)):
        # length = len(temp)
        longest = temp

print(longest)

    
