class account:
    accounts = []
    count = 0
    
    @classmethod
    def input_accounts(cls):
        for i in range(5):
            acc_no = int(input("Enter account number: "))
            
            if acc_no not in cls.accounts:
                cls.accounts.append(acc_no)
                cls.count += 1
            else:
                print("Duplicate ! ")


    @classmethod
    def print_count(cls):
        print(cls.count)

account.input_accounts()                    
account.print_count()