file = open(r"programs\file_handling\data.txt","x")
line = " "

n = 0

while True:
    line = input().strip()
    if(line==""):
        break
    file.write(line+"\n")
    n+=1
print(n)