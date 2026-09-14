def fibonacci():
    a=0
    b=1
    for i in range(0,10):
        c=a
        a=b
        b=c+b
        print(c)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact           

fibonacci()

print(factorial(5))