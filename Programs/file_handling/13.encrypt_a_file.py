def encrypt(str):
    result = "" 
    for char in str:
        if (65<=ord(char)<88 or 97<=ord(char)<120):
            result += chr(ord(char)+3)
        elif (88<=ord(char)<91 or 120<=ord(char)<123):
            result += chr(ord(char)-23)    
        else:
            result += char
    return result

file = open("file1.txt","r")
lines = file.readlines()
file.close()

lines = list(map(encrypt,lines))

file = open("file1.txt","w")
for line in lines:
    file.write(line)
file.close()    


