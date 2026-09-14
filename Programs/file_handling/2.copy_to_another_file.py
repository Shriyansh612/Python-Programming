copy = open("copy.txt","w")
data = open("programs//file_handling//data.txt","r")

text = data.read()
copy.write(text)

data.close()
copy.close()