numbers = [1,3,5,2,4,8,6,9,10]
numbers.sort()
for i in range (0,len(numbers)-1):
    if(numbers[i+1]-numbers[i]!=1):
        print(numbers[i]+1)
        break
