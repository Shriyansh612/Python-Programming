numbers = [0,1,13,8,12,5,6]

def fibonacci_number(n):
    flag=0
    i=0
    j=1
    while(i<=n):
        i,j=j,i+j
        if(j==n):
            flag=1
            break
    if(n==0 or flag==1):
        return True
    else:
        return False

print(list(filter(fibonacci_number,numbers)))            