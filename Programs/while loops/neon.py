n = int(input(print("Enter a number: ")))
sq = n**2
sum = 0
d = 0
while (sq!=0):
    d=sq%10
    sq=sq//10
    sum = sum+d
if (sum==n):
    print("neon")
else:
    print("not neon")        