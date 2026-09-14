def maximum(a,b,c):
    if (a>b):
        if (a>c):
            return a
        elif(c>a):
            return c
    else:
        if(b>c):
            return b
        else:
            return c  

print(maximum(2,4,5))          