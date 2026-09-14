file = open(r"programs\file_handling\data.txt","r")
lines = file.readlines()
file.close()

new_lines = []

for line in lines:
    if (line not in new_lines and line!="\n"):
        new_lines.append(line)

file = open(r"programs\file_handling\data.txt","w")

for line in new_lines:
    file.write(line)

file.close()

print(lines)
print(new_lines)