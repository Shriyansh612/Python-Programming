# tup = (1,1,2,2,2,3,3,4)
# result = ()
# for i in range(len(tup)-1,-1,-1):
#     if(tup[i] not in tup[:i]):
#         result = result+(tup[i],)

# result_final =()

# for i in range(len(result)-1,-1,-1):
#     result_final=result_final+(result[i],)

# print(result_final)            

tup = ((4,8,9),(3,7,2),(1,6,5))

flatten = ()
# print(tup[0][0])
for i in range(len(tup)):
    for j in range(len(tup[i])):
        flatten += (tup[i][j],)

print(flatten)      

# print(tuple(sorted(list(flatten))))

# sorted_flatten = ()
# min = flatten[0]
# for i i

# Bobble sort

temp = list(flatten)

for i in range(len(temp)):
    for j in range(len(temp)-i-1):
        if temp[j] > temp[j + 1]:
            temp[j], temp[j+1] = temp[j+1], temp[j]


# convert back to tuple
flatten = tuple(temp)

print(flatten)
