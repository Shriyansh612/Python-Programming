tup = tuple(map(int,input().split()))

def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False
            
prime_numbers = tuple(filter(prime,tup))

print(prime_numbers)