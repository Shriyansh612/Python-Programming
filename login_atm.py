username = "shriyansh"
password = "Hello123#"
bank_balance = 5000

username1 = input("Enter your username: ")
username1=username1.strip()


if (" " in username1):
    print("Username must not contain any spaces")
elif(username1.lower()!=username):
    print("Username does not match")
else:
    password1 = input("Enter your password: ")
    password1 = password1.strip()

    if (len(password1)>=8):
        # if (password1.isspace()==False):
        if (" " not in password1):
        # if password1.find(" ") == -1:
            c1 = 0      #lower case
            c2 = 0      #upper case
            c3 = 0      #numbers
            c4 = 0      #special symbols
            for i in range (0,len(password1)):
                if(password1[i].islower()):
                    c1+=1
                elif(password1[i].isupper()):
                    c2+=1
                elif(password1[i].isdigit()):
                    c3+=1
                else:
                    c4+=1
            if (c1>0 and c2>0 and c3>0 and c4>0):
                if(password==password1):
                    operation = -1
                    
                    print('''
Enter 1 to check bank balance
Enter 2 to deposit money
Enter 3 to withdraw money
Enter 0 to end the program
''')
                    
                    while(operation!=0):
                        operation = input("Enter: ")  # string input
                        if operation.isdigit():
                            operation = int(operation)
                        else:
                            print("Please Enter a valid number .")
                            continue

                        # operation = int(operation)
                        match operation:

                            case 1:
                                print("Bank Balance:",bank_balance)

                            case 2:
                                deposit = input("Enter amount to be deposited.\n")
                                if (deposit.isnumeric()):
                                    bank_balance = bank_balance + int(deposit)
                                elif(deposit[0]=="-" and deposit[1:].isdigit()):
                                    if (int(deposit)<0):
                                        print("Negative numbers are not allowed\n")    
                                else:
                                    print("Bank Balance must be a number\n")    

                            case 3:
                                withdraw = input("Enter amount to be withdrawn.\n")
                                if (withdraw.isdigit()):
                                    withdraw = int(withdraw)
                                    if (withdraw>bank_balance):
                                        print("Cannot withdraw amount more than bank balance\n")
                                    else:
                                        bank_balance = bank_balance - withdraw
                                else :
                                    print("Bank Balance must be a number\n")

                            case 0:
                                print()    
                            case _:
                                print("Please enter valid input\n")
                    if (operation==0):
                        print("Thank you for using ATM")                                                

                else:
                    print("Password do not match")
            else:
                print('''
Password must contain 
atleast 1 uppercase character
atleast 1 lowercase character
atleast 1 number
atleast 1 special symbol                                                                                                              )                             
''')
        else:
            print("Password cannot contain spaces")
    else:
        print("Password must be atleast 8 characters long")                            