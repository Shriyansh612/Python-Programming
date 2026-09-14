numbers = ["1",2,3,"4","hello","5.6"]
new_numbers = []

for i in range(len(numbers)):
    try:
        numbers[i] = int(numbers[i])
    except ValueError:
        print("Value Error for",numbers[i])
    else:
        new_numbers.append(numbers[i])
print(new_numbers)                
              