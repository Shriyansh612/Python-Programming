n = int(input(print("Enter a number: ")))
n1 = n 
a = 0
m = 0
while (n!=0):
    a = n%10
    m = m*10+a
    n = n//10
print (m) 
if (m==n1):
    print ("palindrome")
else:
    print ("not palindrome")  