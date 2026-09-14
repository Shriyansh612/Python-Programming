n = int(input("Enter a number:: "))
sq = n*n
num_digits = 0
n1 = n
while (n!=0):
    num_digits += 1
    n=n//10
'''    
last = 0
for i in range (1,num_digits+1):
    last = last*10+(sq%10)
    sq=sq//10
rev = 0
while(last!=0):
    rev = rev*10+(last%10)
    last = last //10
'''        
rev = sq%(10**num_digits)
if (rev == n1):
    print("It is an automorphic number")
else:
    print("It is not an automorphic number")             