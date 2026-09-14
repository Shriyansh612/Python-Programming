numbers = list(map(int,input().split()))

maj_element = None

for i in range(0,len(numbers)):
    if(numbers.count(numbers[i])>len(numbers)/2):
        maj_element = numbers[i]
        break

if(maj_element):
    print("Majority Element:",maj_element)
else:
    print("No Majority")    