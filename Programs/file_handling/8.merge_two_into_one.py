file1 = open("copy.txt","r")
file2 = open("demo.txt","r")

lines1 = file1.readlines()
lines2 = file2.readlines()

file1.close()
file2.close()

new_lines = []

for line in lines1:
    if (line not in new_lines and line!="\n"):
        new_lines.append(line)

new_lines.append("\n")

for line in lines2:
    if (line not in new_lines and line!="\n"):
        new_lines.append(line)

data = open("programs\\file_handling\\data.txt","w")
for line in new_lines:
    data.write(line)

data.close()            