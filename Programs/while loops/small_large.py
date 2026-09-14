n = int(input(print("Enter a number: ")))
sm = 9
lr = 0
dig = 0
while (n!=0):
    dig=n%10
    if (dig<sm):
        sm = dig
    if (dig>lr):
        lr = dig 
    n=n//10    
print("Smallest Digit:", sm)
print("Largest Digit:", lr)
