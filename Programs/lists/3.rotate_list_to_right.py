numbers = []        #defining empty list
numbers.extend(input("Enter numbers separated by space: ").split())     #inputing list items separated by spaces
numbers = list(map(lambda n:int(n),numbers))  #converting list elements to int from string

k = int(input("Enter the amount to turn it right by: "))

print(numbers[-k:]+numbers[:-k])