#to check whether two lists have same unique elements
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

A = set(list1)
B = set(list2)

if(A == B):
    print("Two lists contain the same unique elements")
else:
    print("Two lists does not contain the same unique elements")    

