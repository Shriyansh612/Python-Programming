purchase = input("Enter purchase amount: ")
if (purchase.isdigit()):
    if (purchase<0):
        print("Please enter valid purchase amount")    
    type_of_customer = input("Enter Yes for Premium Customer and No for Normal Customer")
    type_of_customer = type_of_customer.lower()
    if ((type_of_customer!="yes") and (type_of_customer != "no")):
        print("Please enter Yes for Premium Customer and No for Normal Customer")
    else:    
        if (purchase>=5000):
            if(type_of_customer == "yes"):
                dis = 0.2*purchase
                print("Discount:", dis)
                print("Total bill:", purchase-dis)
            else:
                dis = 0.1*purchase
                print("Discount:", dis)
                print("Total bill:", purchase-dis)
        elif (purchase>=2000):
            if(type_of_customer == "yes"):
                dis = 0.1*purchase
                print("Discount:", dis)
                print("Total bill:", purchase-dis)
            else:
                dis = 0.05*purchase
                print("Discount:", dis)
                print("Total bill:", purchase-dis) 
        elif (purchase<2000):
            if(type_of_customer == "yes"):
                dis = 0.05*purchase
                print("Discount:", dis)
                print("Total bill:", purchase-dis)
            else:
                dis = 0
                print("Discount:", dis)
                print("Total bill:", purchase-dis) 
else:
    print("Please enter valid purchase amount")                