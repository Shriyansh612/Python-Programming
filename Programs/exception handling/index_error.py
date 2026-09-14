numbers = [1,2,3,4,5]
try:
    for i in range(10):
        print(numbers[i])
except IndexError:
    print("List only contains 5 elements")        