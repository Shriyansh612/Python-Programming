cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))
if (sp>cp):
    print(f"Profit: {(sp-cp):.2f}")
elif (cp>sp):
    print(f"Loss: {(cp-sp):.2f}")
else:
    print("Neither profit nor loss")        