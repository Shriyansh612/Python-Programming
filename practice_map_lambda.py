#1


#2
# numbers = [[1,2],[3,4]]

# # print(list(map(lambda n:n*2,map(lambda row:row,numbers))))

# result = list(map(lambda row: list(map(lambda n:n*2, row)), numbers))
# print(result)

# new_numbers = [[0,0],[0,0]]
# for i in range(0,2):
#     new_numbers[i]=list(map(lambda n : n*2,numbers[i]))

# print(new_numbers)   


#4

# def vowels2(word):
#     c=0
#     for chr in word:
#         if (chr in'aeiou'):
#             c+=1
#     if(c>2):
#         return word

# words = ["hello","nature","mathematics","computer","normal"]

# print(list(filter(vowels2,words)))

#5

# numbers = [1,4,9,0,-9,-1]

# print(list(map(lambda n : n**(0.5),list(filter(lambda n:n>0,numbers)))))

#6

# students = ["Mohan","Rahul","Naman","Kartik"]

# student_marks = [32,56,45,76]

# print(list(map(lambda n : n+5 if n>=33 else n,student_marks)))

#7

# product_prices = [1200,400,800,1500]

# products_above_1000 = list(filter(lambda n:n>1000,product_prices))

# print(list(map(lambda n:n*1.18, products_above_1000)))

#30

# numbers = [1,3,4,12,18,6,7,14]

# even_numbers = list(filter(lambda n:n%2==0,numbers))

# print(even_numbers)

# square_even_numbers = list(map(lambda n:n**2,even_numbers))
# print(square_even_numbers)

# greater_than_100 = list(filter(lambda n:n>100,square_even_numbers))
# print(greater_than_100)

# print(sorted(greater_than_100,reverse=True))

#29

# numbers = [13,31,43,56,77,23,32]

# def reverse(n):
#     rev=0
#     while(n!=0):
#         rev=rev*10+(n%10)
#         n=n//10
#     return rev

# result = list(filter(lambda n:n if(reverse(n) in numbers) else None,numbers))
# print(result)

# result=list(filter(lambda x:int(str(x)[::-1])in numbers, numbers))

# print(result)

products = [
    ["Laptop", 50000],
    ["Mouse", 800],
    ["Keyboard", 1500],
    ["Monitor", 12000],
    ["Pen", 50]
]

filtered_products = list(filter(lambda product : product[1]>1000,products))
print(filtered_products)

final_price = list(map(lambda product : [product[0],product[1]*0.8], filtered_products ))
print(final_price)

#24


# print(bin(7))

# numbers = [7,15,31,6,5,8,10]

# result = list(filter(lambda n : bin(n)[2:].count("1")>3,numbers))
# print(result)


# def check(number):
#     binary = bin(number)

#     if binary[2:].count("1") > 3:
#         return True
#     else:
#         return False

# result = list(filter(check, numbers))

# print(result)


numbers = [[1, 2], [3, 4]]

# [1,2, 3, 4]
flatten = []

for row in numbers:
    flatten.extend(row)

print(list(filter(lambda n:n%2==0,flatten)))