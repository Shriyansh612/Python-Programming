# 9.   Build a Mini Notepad (Terminal-Based)

# Features:

# 1.Create File
# 2.Open File
# 3.Edit File????
# 4.Save
# 5.Save As
# 6.Search
# 7.Replace
# 8.Exit

file_names = open("file_names.txt","a+")
file_names.seek(0)
names = file_names.readlines()

names = list(map(lambda text:text.strip(),names))

def create():
    name = input("Enter file name: ")+".txt"
    if (name in names):
        print("A file by this name already exists")
        return False
    else:
        file_names.write(name+"\n")
        names.append(name)
        file = open(name,"x")
        file.close()
        print("File Created")
        return True

def open_file():
    name = input("Enter file name: ")+".txt"
    if (name not in names):
        print("No file exists by such name")
        return False,None
    else:
        file = open(name,"r+")
        print("File opened")
        return True,file
    
def save(file):
    file.close()
    print("File Saved")

def search(file):
    lines = file.readlines()

    word = input("Enter word to be searched for: ")
    freq = 0

    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            if (word == words[j]):
                print(f"Line No.{i+1} and Word No.{j+1}")
                freq+=1
    if (freq == 0):
        print("Not Found")                    

def replace(file):
    lines = file.readlines()
    file.seek(0)

    to_replace = input("Enter word to be replaced: ")
    replace_with = input("Enter word to replace by: ")

    file.truncate()

    for i in range(len(lines)):
        words = lines[i].split()
        new_line = ""
        for j in range(len(words)):
            if (words[j]==to_replace):
                words[j]=replace_with
            new_line = new_line+words[j]+" "
        new_line = new_line.strip()
        file.write(new_line+"\n")            

    print("Word replaced successfully")        


def edit(file):
    lines = file.readlines()

    line_num = int(input("Enter line number: "))
    if (line_num > len(lines) or line_num<=0):
        print("Invalid Line Number")
        return
    
    word = input("Enter word: ")
    if (word in lines[line_num-1]):
        word_index = lines[line_num-1].find(word)
        new_word = input("Enter new word: ")
        newline = (lines[line_num-1][:word_index]+new_word+lines[line_num-1][word_index+len(word):]) 
        lines[line_num-1] = newline
        # file = open("test.txt","w")
        file.seek(0)
        for line in lines:
            file.write(line)
        file.truncate()
        print("Edit Successful")            
    else:
        print("word not found")

def append(file):
    file.read()

    new_data = input("Enter more data: ")
    file.write("\n")
    file.write(new_data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

print("""
Enter operation:
To create a new file: 1
To open a file: 2
To see all files: 3
To close: 0                        
""")

op = -1

while (op!=0):
    op = int(input("Enter operation: "))
    match op:
        case 1:
            create()
        case 2:
            nat,file = open_file()
            if (nat):
                op1=-1
                print('''
Enter option:
To display content: 1
To search for a word: 2
To replace a word: 3
To save: 4
To save as: 5 
To edit: 6
To enter more data: 7                     
To close: 0                                                                                           

    ''')
                while(op1!=0):
                    op1 = int(input("Enter option: "))
                    match op1:
                        case 1:
                            file.seek(0)
                            data = file.read()
                            print(data)
                        case 2:
                            file.seek(0)
                            search(file)
                        case 3:
                            file.seek(0)
                            replace(file) 
                        case 4:
                            save(file)
                            break 
                        case 5:
                            file.seek(0)
                            data = file.read()
                            new_name = input("Enter new name: ")+".txt"
                            if (new_name not in names):
                                file.close()
                                file_names.write(new_name+"\n")
                                names.append(new_name)
                                new_file = open(new_name,"x")
                                new_file.write(data)
                                save(new_file)
                                break
                            else:
                                print("File by that name already exists")
                        case 6:
                            file.seek(0)
                            edit(file)

                        case 7:
                            file.seek(0)                                                            
                            append(file)
                        case 0:
                            save(file)
                            print()               
        case 3:
            print(names)
        case 0:
            print("Thank You")            

file_names.close()