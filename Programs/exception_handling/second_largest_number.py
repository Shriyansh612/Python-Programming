n = -1
numbers = []
while(n!=0):
    try:
        n = int(input("Enter an integer: "))
        numbers.append(n)
    except ValueError:    
        continue

print("Second largest: ",sorted(numbers)[-2])
