numbers = [1,2,3,4,5]
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return True
    else:
        return False

filtered_numbers = list(filter(prime,numbers))
print(filtered_numbers)

print(list(map(lambda n:n**3,filtered_numbers)))