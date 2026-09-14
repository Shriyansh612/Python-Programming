n = int(input(print("Enter a number: ")))
c=0
for i in range (1,n+1):
    if (n%(i*(i+1))==0):
        c=c+1
if (c>0):
    print ("pronic")
else:
    print ("not pronic")   