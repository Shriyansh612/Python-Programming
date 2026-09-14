num = int(input("Enter number of sets: "))
sets = []

for i in range(num):
    sets.append(set(map(int,input().split())))

intersection = sets[0]

for i in range(1,num):
    intersection = intersection & sets[i]

print(intersection)    