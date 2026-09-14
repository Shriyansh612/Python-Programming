def alpha(str1,str2):
    s1 = str1.lower()
    s2 = str2.lower()

    if (s1==s2):
        return str1,str2
    elif (s1 in s2):
        return s1,s2
    elif (s2 in s1):
        return s2,s1

    for i in range(min(len(s1),len(s2))):
        if (97<=ord(s1[i])<123 and 97<=ord(s2[i])<123):
            if (ord(s1[i])>ord(s2[i])):
                return str2,str1
            elif (ord(s1[i])<ord(s2[i])):
                return str1,str2
            else:
                continue
        else:
            continue    

file = open("file1.txt","r")
lines = file.readlines()
file.close()

for line in lines:
    if (line=="\n"):
        lines.remove(line)

# lines.sort()        

for i in range(len(lines)):
    for j in range(len(lines)-i-1):
        lines[j],lines[j+1] = alpha(lines[j],lines[j+1])

file = open("file1.txt","w")
for line in lines:
    if(line[-1]!="\n"):
        file.writelines(line+"\n")
    else:
        file.writelines(line)    
file.close()            
