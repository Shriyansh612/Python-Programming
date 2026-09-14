num = int(input("Enter a number: "))
def armstrong(n):
    n1=n
    sum = 0
    while(n!=0):
        sum = sum+(n%10)**3
        n=n//10
    if (sum==n1):
        print("armstrong")
    else:
        print("not armstrong")      

armstrong(num)          