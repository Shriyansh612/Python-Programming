numbers = list(map(int,input().split()))
target = int(input("Enter target number: "))

for i in range(0,len(numbers)):
    for j in range(i+1,len(numbers)):
        if (numbers[i]+numbers[j]==target):
            print(f"{numbers[i]}+{numbers[j]}={target}")