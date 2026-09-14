A = set(map(int,input().split()))
B = set(map(int,input().split()))

intersection = set()

for n in A:
    if(n in B):
        intersection.add(n)

print(intersection)        