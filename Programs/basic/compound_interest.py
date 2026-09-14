principal_amount = float(input("Enter principal amount: "))
rate = float (input("Enter rate of interest: "))
time = int (input("Enter number of years: "))
amount = principal_amount*((1+rate/100)**time)
print(f"Total Amount: {amount:.4f}")
print(f"Compound Interest: {(amount-principal_amount):.4f}")



# name = "Roshan"
# age = 21

# # print("Hello! i am ",name,"my age is", age)

# #  F string

# print("Hello!, My Name is {name} and i am a {age}")