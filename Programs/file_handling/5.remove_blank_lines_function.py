file = open(r"programs\file_handling\data.txt","r")
lines = file.readlines()
file.close()

file = open("demo.txt","w")

for line in lines:
    if line.strip() != "":
        file.write(line)

file.close()
print(lines)