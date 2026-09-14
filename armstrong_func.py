def cubesum(n):     #to calculate sum of cubes of individual digits
    sum = 0
    while(n!=0):
        sum = sum+(n%10)**3
        n=n//10
    return sum

def PrintArmstrong():       #to print armstrong numbers between 1 and 1000
    print("Armstrong numbers between 1 and 1000: ")
    for i in range(1,1001):
        if(i==cubesum(i)):
            print(f"{i} is an Armstrong number")

def isArmstrong(n):     #to check whether a number is an armstrong or not
    if (n==cubesum(n)):
        return True
    else:
        return False
    
PrintArmstrong()

num = int(input("Enter a number: "))

print(isArmstrong(num))    