n = int(input(print("Enter a number: ")))
d = 0
c = 0
while (n!=0):
    d=n%10
    n=n//10
    if (d==0):
        c=c+1
print ("No. of Zeroes:", c)
if (c>0):
    print ("duck") 
else:
    print ("not duck")       