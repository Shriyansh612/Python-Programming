numbers = list(map(int,input().split()))

A = set()
for num in numbers:
    if(num in A):
        print(num)
        break
    else:
        A.add(num)