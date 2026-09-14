tup = (1,2,3,4,5,6)

deflatten = []
for i in range(0,len(tup),2):
    row = ()
    row += (tup[i:i+2])
    deflatten.append(row)

print(tuple(deflatten))   