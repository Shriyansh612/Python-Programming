numbers = list(map(int,input().split()))

# for i in range(0,len(numbers)):

# print(numbers)

largest = numbers[0]
sec_largest = numbers[1]
if(largest<sec_largest):
    largest = numbers[1]
    sec_largest = numbers[0]

for i in range(2,len(numbers)):
    if(numbers[i]>largest):
        sec_largest = largest
        largest = numbers[i]
        

print("largest:",largest)
print("second largest:",sec_largest)               