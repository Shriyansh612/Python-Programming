file = open("file2.txt","r")
lines = file.readlines()
file.close()

for i in range(len(lines)):
    for j in range(len(lines)-i-1):
        if (len(lines[j])>len(lines[j+1])):
            lines[j],lines[j+1] = lines[j+1],lines[j]            

file = open("file2.txt","w")
for line in lines:
    file.write(line)
file.close()    