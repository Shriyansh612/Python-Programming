import math
n = int(input("Enter number: "))
r = int(input("Enter number: "))

def permutation(num,index):
    if (num>=0 and index>=0 and index<=num):
        return math.factorial(num)//math.factorial(num-index)
    else:
        print("Invalid Input")

def combination(num,index):
    if (num>=0 and index>=0 and index<=num):
        return math.factorial(num)//(math.factorial(index)*math.factorial(num-index))
    else:
        print("Invalid Input")

print(f"Permutation {n}P{r}:",permutation(n,r))
print(f"Combination {n}C{r}:",combination(n,r))


