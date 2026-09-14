for n in range (1, 101): 
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
