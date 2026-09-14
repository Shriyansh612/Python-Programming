numbers =[13,31,43,34,77,233,4144,87]

result = list(filter(lambda n : int(str(n)[::-1]) in numbers,numbers))
print(result)