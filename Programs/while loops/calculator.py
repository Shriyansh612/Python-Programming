a = 1
while (a==1):
    n = int(input(print("Enter number: ")))
    op = input(print("Enter operation"))
    m = int(input(print("Enter number: ")))
    if (op=="+"):
        print(n+m)
    elif(op=="-"):    
        print(n-m)
    elif(op=="*"):    
        print(n*m)
    elif(op=="/"):
        print(n/m)    
    a = int(input(print("1 for furthur\n2 for stop")))