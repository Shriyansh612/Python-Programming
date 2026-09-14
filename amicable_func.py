def sum_proper_divisors(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    return sum

def amicable(n1,n2):
    if (sum_proper_divisors(n1)==n2 and sum_proper_divisors(n2)==n1):
        print("The two numbers are amicable numbers")
    else:
        print("The two numbers are not amicable numbers")                

num1 = int(input("Enter a number: "))        
num2 = int(input("Enter a number: "))

amicable(num1,num2)