#  filter()
#  kisi condition ko check karnta hai or sirf wahi element rakhta hai jo condition ko satisft karta hai


# numbers = [1,2, 3, 4, 5, 6]

# even = lambda num : num if (num%2==0) else None

# even_numbers = lambda numbers1 : list(map(even,numbers1))

# result = filter(lambda numbers: numbers%2==0, numbers)   # filter(function, iterable)

# print(list(result))



# numbers = [5, 12, 7, 18, 3, 20]

# result = filter(lambda num:num>10,numbers)

# print(list(result))


# names = ["Shriyansh","Raghu","Ravi","Virat","Rohit","Abhishek"]

# result = filter(lambda name:len(name)>5,names)

# print(list(result))

# def prime(n):
#     c=0
#     for i in range(1,n+1):
#         if(n%i==0):
#             c+=1
#     if(c==2):
#         return True
#     else:
#         return False

# numbers = [1,2,3,4,5,6,7,8,9]

# result = filter(lambda num:prime(num),numbers)

# print(list(result))

numbers = [1,2,3,4]

condition = lambda n : n**2 if(n%2==0) else n**3

result = list(map(condition,numbers))

print(list(map(lambda n: n**2 if n%2==0 else n**3, numbers)))

