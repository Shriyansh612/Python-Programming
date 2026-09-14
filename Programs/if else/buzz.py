n = int(input(print("Enter a number: ")))
n1 = n
dig = n%10
if (dig==7 or n1%7==0):
    print ("buzz number")
else:
    print ("not a buzz number")