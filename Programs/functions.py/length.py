text = input("Enter a string: ")
def length (text):
    temp = ""
    len=0
    while (temp!=text):
        temp=temp+text[len]
        len+=1
    return len

print(length(text))    