numbers = list(map(int,input().split()))

max_sum = float('-inf')
sub_array = []

for i in range(len(numbers)):
    for j in range(i,len(numbers)):
        temp = []
        temp = numbers[i:j+1]
        print(temp,":",sum(temp))
        if(sum(temp)>max_sum):
            max_sum = sum(temp)
            sub_array = temp


print(f"Sub-Array with maximum sum is {sub_array} and sum is {max_sum}")            


# arr = [1, -2, 6, -1, 3]


# [1] =
# [1, -2] = -
# [1, -2, 6] = 
# [1, -2, 6, -1] 
# [1, -2, 6, -1, 3] = 
# [-2] = -
# [-2, 6] = 
# [-2, 6, -1] = 
# [-2, 6, -1, 3] = 
# [6] = 
# [6, -1] = 
# [6, -1, 3] = 
# [-1] = -
# [-1, 3] = 
# [3] = 

# Maximum Subarray Sum = 8