file = open(r"programs\file_handling\data.txt","r")
lines = file.readlines()
file.close()

keyword = input("Enter keyword: ")

for line in lines:
    if(keyword in line):
        print(line,end="")

print(lines)