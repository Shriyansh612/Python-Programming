a = int(input(print("Enter a number: ")))
b = int(input(print("Enter a number: ")))
c = 0
d = 0
for i in range (1,a+1):
    if (a%i==0):
        c=c+1
for j in range (1,b+1):
    if (b%j==0):
        d=d+1
if (c==2 and d==2 and abs(a-b)==2):
    print ("They are twin prime numbers")             
else:
    print ("They are not twin prime numbers") 