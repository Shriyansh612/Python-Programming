A = set(map(int,input().split()))

for i in range(1,max(A)):
    if (i not in A):
        print(i)
        break   