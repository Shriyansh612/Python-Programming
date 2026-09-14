a = float(input("Enter a side of triangle: "))
b = float(input("Enter a side of triangle: "))
c = float(input("Enter a side of triangle: "))
if((a+b)>c and (b+c)>a and (c+a)>b):
    print("It is a valid triangle")
else:
    print("It is not a valid triangle")    