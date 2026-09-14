file = open("num.txt","r")
try:
    sum = 0
    numbers = file.readlines()
    for num in numbers:
        sum += int(num.strip())
except ValueError:
    print("File must only contain numbers")
else:
    print("sum:",sum)            