file = open(r"programs\file_handling\data.txt","r")

data = ""

while (True):
    temp = file.readline()
    if (temp=="\n"):
        continue
    elif (temp==""):
        break
    data+=temp

file.close()

file = open(r"programs\file_handling\data.txt","w")
file.write(data)

file.close()