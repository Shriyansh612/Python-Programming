def decrypt(str):
    result = ""
    for char in str:
        if (68<=ord(char)<91 or 100<=ord(char)<123):
            result += chr(ord(char)-3)
        elif (65<=ord(char)<98 or 97<=ord(char)<100):
            result += chr(ord(char)+23)
        else:
            result += char
    return result

file = open("file1.txt","r")
lines = file.readlines()
file.close()

lines = list(map(decrypt,lines))

file = open("file1.txt","w")
for line in lines:
    file.write(line)
file.close()    