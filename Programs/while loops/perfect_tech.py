n = int(input(print("Enter a number: ")))
ch = int(input(print("Enter choice: 1 or 2")))
match ch:
    case 1:
        sum = 0
        n1 = n
        for i in range(1,n):
            if(n%i==0):
                sum = sum + i
        if (sum==n1):
            print("perfect")
        else:
            print("not perfect") 
    case 2:
        n1 = n
        num = 0
        while (n!=0):
            n=n//10
            num = num+1
        if (num%2!=0):
            print("it is not a tech number")
        else:
            a = n1%(10**(num/2))
            b = n1//(10**(num/2))
            if ((a+b)**2==n1):
                print("tech")
            else:
                print ("it is not a tech number")

                