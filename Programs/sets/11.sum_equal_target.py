A = set(map(int,input().split()))
B = set(map(int,input().split()))
target = int(input("Enter target number: "))

for n in A:
    for m in B:
        if(n+m==target):
            print(f"{n}+{m}={target}")