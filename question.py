print('''
Length of string: 0<N<=2*10^5
Number of queries: 0<N<=10^5
Length of string must be equal to N
0<=L<=R<N
''')

first_line = input("Enter length of string and number of queries followed by a space: ")

N = int(first_line[:first_line.find(" ")])
Q = int(first_line[first_line.rfind(" "):])

S = input("Enter string of digits (0-9): ")

if (not 0<N<=2*10**5 or not 0<Q<=10**5 or not len(S)==N):
    print("Please enter valid input")
else:
    print("For each query enter L and R both inclusive separated by space")
    for i in range(Q):
        query = input("Enter query: ")
        L = int(query[:query.find(" ")])
        R = int(query[query.rfind(" "):])

        if (not 0<=L<=R or not L<=R<N):
            print("Invalid query input")
        else:
            if(int(S[L:R+1])%8==0):
                print("YES")    
            else:
                print("NO")    
