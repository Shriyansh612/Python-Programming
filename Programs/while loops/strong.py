n = int(input("Enter a number: "))
n1 = n
sum = 0
dig = 0
fac = 1
while (n!=0):
    dig = n%10
    n = n//10
    for i in range (1,dig+1):
        fac = fac*i
    sum += fac
    fac = 1
if (sum == n1):
    print("Strong Number")
else:
    print("Not a strong number")            
        