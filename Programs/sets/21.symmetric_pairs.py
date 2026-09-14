A = {(1,2),(3,4),(2,1),(5,6),(7,8),(6,5)}
temp = set()

for element in A:
    if (element[::-1] in A and element[::-1] not in temp):
        temp.add(element)
        print(element,":",element[::-1])