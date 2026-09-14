n = int(input(print("Enter a number: ")))
a = 0
for i in range (1, n+1):
    if (n%i==0):
        a=a+1
if (a==2):
    print("It is a prime number")
else:
     print ("It is not a prime number")           