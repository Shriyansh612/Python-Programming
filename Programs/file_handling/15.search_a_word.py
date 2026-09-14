file = open("file1.txt","r")
lines = file.readlines()
file.close()

word = input("Enter word to be searched for: ")

for i in range(len(lines)):
    words = lines[i].split()
    for j in range(len(words)):
        if (word == words[j]):
            print(f"Line No.{i+1} and Word No.{j+1}")