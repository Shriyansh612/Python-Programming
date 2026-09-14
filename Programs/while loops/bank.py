print('''
Welcome to Bank
''')
name = input("Enter your name: ")
bank_balance = int(input("Enter your bank balance: "))
print('''
To deposit money press 'D'
To withdraw money press 'W'
To check bank balance press 'C'
To end press 'E'      
''')
operation = input("")
while (operation!="E"):
    match operation:
        case "D":
            amount = int(input("Enter amount to be deposited: "))
            bank_balance += amount
        case "W":
            amount = int(input("Enter amount to be withdrawn: "))
            bank_balance -=amount
        case "C":
            print("Current Bank Balance:", bank_balance)
    operation = input("")        
print("Thank You")            