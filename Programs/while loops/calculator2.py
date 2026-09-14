print('''
    CALCULATOR

 PRESS S TO START
  PRESS E TO END
PRESS R TO RESTART
''')
op = input("")
if(op!="S"):
    print("Thank you for using calculator!")
else:
    m = float(input(""))    
while(op=="S"):
    op = input("")
    if (op=="E"):
        print("Thank you for using calculator!")
        break
    if (op=="R"):
        m = float(input(""))
        op = input("")    
    n = float(input(""))
    match op:
        case "+":
            print(m+n)
            m = m+n
        case "-":
            print(m-n)
            m = m-n
        case "*":
            print(m*n)
            m*=n
        case "/":
            print(m/n)
            m/=n
        case "^":
            print(m**n)
            m**=n
    op = "S"  