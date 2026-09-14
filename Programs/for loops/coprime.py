a = int(input(print("Enter a number: ")))
b = int(input(print("Enter a number: ")))
c=0
hcf=1
for i in range (2,min(a,b)+1):
    if (a%i==0 and b%i==0):
        c=c+1
        hcf=i
if (c>0):
    print ("They are not co prime") 
else:
    print ("they are co prime")           
print ("Their HCF is ", hcf)    