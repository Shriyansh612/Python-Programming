num = int(input("Enter a number: "))


def sum_digits(n):
    sum = 0
    while(n!=0):
        sum = sum+(n%10)
        n=n//10
    return sum

def power_sum_digits(n1):
    sum=0
    while(n1!=0):
        sum = sum+((n1%10)**2)
        n1=n1//10
    return sum

def reverse (n2):
    rev=0
    while(n2!=0):
        rev=rev*10+(n2%10)
        n2=n2//10
    return rev

def binary (n3):
    bin = 0
    while(n3!=0):
        bin = bin*10+(n3%2)
        n3=n3//2
    bin = reverse(bin)
    return bin
    
print(sum_digits(num))
print(power_sum_digits(num))
print(reverse(num))
print(binary(num))
