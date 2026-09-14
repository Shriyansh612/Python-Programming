numbers = list(map(int,input().split()))
A = set()
duplicate = []

for num in numbers:
    if(num in A and num not in duplicate):
        duplicate.append(num)
    else:
        A.add(num)    

print(duplicate)        