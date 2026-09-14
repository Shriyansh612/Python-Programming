A = set(map(int,input().split()))
B = set(map(int,input().split()))

a = B - A
b = A - B
print("Missing in A:",a)
print("Missing in B:",b)
