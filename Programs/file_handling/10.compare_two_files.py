file1 = open("file1.txt","r")
lines1 = file1.readlines()
file1.close()

file2 = open("file2.txt","r")
lines2 = file2.readlines()
file2.close()

l1 = []
l2 = []

for line in lines1:
    if (line not in l1 and line!="\n"):
        l1.append(line)

for line in lines2:
    if (line not in l2 and line!="\n"):
        l2.append(line) 

print(l1)
print(l2)               

if (l1 == l2):
    print("Same Lines")
else:
    flag = 0
    if (len(l1)>=len(l2)):
        temp = []
        for line in l1:
            if (line in l2):
                temp.append(line)
        if (temp == l2):
            print("Missing Lines")
        else:
            print("Different Lines")
    else:
        temp=[]
        for line in l2:
            if (line in l1):
                temp.append(line)
        if(temp == l1):
            print("Missing Lines")
        else:
            print("Unique Lines")                                                