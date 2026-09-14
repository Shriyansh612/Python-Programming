num=int(input("Enter a number: "))

def prime(n):
    a = 0
    for i in range (1, n+1):
        if (n%i==0):
            a=a+1
    if (a==2):
        print("It is a prime number")
    else:
        print ("It is not a prime number") 

prime(num)        

def pronic (n):
    c=0
    for i in range (1,n+1):
        if (n%(i*(i+1))==0):
            c=c+1
    if (c>0):
        print ("pronic")
    else:
        print ("not pronic")    

pronic(num)

def buzz(n):
    n1 = n
    dig = n%10
    if (dig==7 or n1%7==0):
        print ("buzz number")
    else:
        print ("not a buzz number")  

buzz(num)

def automorphic(n):
    sq = n*n
    num_digits = 0
    n1 = n
    while (n!=0):
        num_digits += 1
        n=n//10
    rev = sq%(10**num_digits)
    if (rev == n1):
        print("It is an automorphic number")
    else:
        print("It is not an automorphic number") 

automorphic(num)

def duck(n):
    d = 0
    c = 0
    while (n!=0):
        d=n%10
        n=n//10
        if (d==0):
            c=c+1
    if (c>0):
        print ("duck") 
    else:
        print ("not duck")  

duck(num)

def happy(n):
    sum = 0
    n1 = n
    n2 = n
    while(n1>=6):
        while (n!=0):
            sum =sum + ((n%10)**2)
            n=n//10
        n = n1
        n1 = sum
        sum = 0
    if (n1==1):
        print(n2, "Happy")
    else:
        print(n2, "not happy")

happy(num)

def neon(n):
    sq = n**2
    sum = 0
    d = 0
    while (sq!=0):
        d=sq%10
        sq=sq//10
        sum = sum+d
    if (sum==n):
        print("neon")
    else:
        print("not neon")  

neon(num)

def palindrome(n):
    n1 = n 
    a = 0
    m = 0
    while (n!=0):
        a = n%10
        m = m*10+a
        n = n//10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    if (m==n1):
        print ("palindrome")
    else:
        print ("not palindrome") 

palindrome(num)

def perfect(n):
    sum = 0
    n1 = n
    for i in range(1,n):
        if(n%i==0):
            sum = sum + i
    if (sum==n1):
        print("perfect")
    else:
        print("not perfect") 

perfect(num)