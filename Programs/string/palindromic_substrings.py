text = input("Enter string: ")
length = len(text)
string = ""
rev_string = ""
for i in range (1,length+1):
    for j in range (0,length+1-i):
        string = text[j:j+i]
        rev_string = string[::-1]
        if (string==rev_string):
            print(string)
