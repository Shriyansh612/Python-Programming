maximum = lambda a,b,c : a if (a>b and a>c) else b if (b>a and b>c) else c if (c>a and c>b) else "Two or more are equal and maximum"  # ternary operator

# print(maximum(3,5,5))

abc = lambda x :x+1

# loop
#multiple statement
 # assingment
 # if else


def square(num):
    return num * num

numbers =[1,2,3,4]

result = map(square, numbers)

# print(list(result))

# square(numbers) 

square_list = lambda num : list(map(square,num))

# print(square_list(numbers))


names = ["shriyansh","raghu","ravi"]

upper = lambda name: name.upper()

upper_list = lambda names1:list(map(upper,names1))

print(upper_list(names))