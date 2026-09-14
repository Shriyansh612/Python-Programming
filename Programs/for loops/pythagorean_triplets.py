for i in range (3,51):
    for j in range (2, i):
        for k in range (1,j):
            if (((i**2+j**2)==k**2 or (j**2+k**2)==i**2 or (k**2+i**2)==j**2) and i!=j and j!=k and k!=i):
                print(k, j ,i)