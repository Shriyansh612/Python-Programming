basic = int(input("Enter basic salary: "))
if (basic<= 10000):
    hra = 0.2*basic
    da = 0.8*basic
    print("HRA is:", hra)
    print("DA is:", da)
    print("Gross Salary: ", hra+da+basic)
elif (basic<=20000):
    hra = 0.25*basic
    da = 0.9*basic
    print("HRA is:", hra)
    print("DA is:", da)
    print("Gross Salary: ", hra+da+basic)
elif (basic>20000):
    hra = 0.3*basic
    da = 0.95*basic
    print("HRA is:", hra)
    print("DA is:", da) 
    print("Gross Salary: ", hra+da+basic)   
