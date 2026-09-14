numbers = [1,153,36,407,41]

def armstrong(n):
    sum=0
    n1=n
    while(n!=0):
        sum=sum+(n%10)**3
        n=n//10
    if(n1==sum):
        return True
    else:
        return False        

armstrong_numbers = list(filter(armstrong,numbers))
print(armstrong_numbers)

print(sorted(armstrong_numbers,reverse=True))