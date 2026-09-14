text = input("Enter email: ")
c=0
l = len(text)
for char in text:
    if (char==" "):
        c+=1
if (c>0):
    print("Spaces are not allowed in email")
else:
    if (text[slice(l-10,l)]=="@gmail.com"):
        print("Valid email")
    else:
        print("Invalid email")        
