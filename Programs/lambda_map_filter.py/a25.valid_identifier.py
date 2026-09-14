def valid_identifier(word):
    c=0     #for special symbols other than underscore
    for char in word:
        if (char.isalpha()):
            pass
        elif(char.isdigit()):
            pass
        elif(char.isspace()):
            pass
        elif(char=="_"):
            pass
        else:
            c+=1
            break
    if(c==0 and word[0].isdigit()==False):
        return True
    else:
        return False

words = ["1n","n","hello_python","hello#python"]

print(list(filter(valid_identifier,words)))