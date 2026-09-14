n = int(input(print("Enter a number: ")))
digit = 0
dig = 0
rev = 0
while (n!=0):
    digit = digit + 1
    dig = n%10
    n=n//10
    rev = rev*10+dig
print ("Number of digits: ", digit)
while (rev!=0):
    print(rev%10)
    rev=rev//10