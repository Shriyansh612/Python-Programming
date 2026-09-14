numbers = [1,2,3,4,5]
try:
    index = int(input("Enter list index to display its value: "))
    if (index>=len(numbers) or index<0):
        raise ValueError
except ValueError:
    print("Invalid list index")
else:
    print("Value:",numbers[index])    