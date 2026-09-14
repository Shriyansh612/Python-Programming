num = list(map(int,input().split()))

num1 = []
for i in range(0,len(num)):
    if(num[i] not in num[i+1:]):
        num1.append(num[i])

print(num1)        