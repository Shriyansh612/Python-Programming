str = input("Enter string: ")
rev = ""
l = len(str)
for i in range (l-1,-1,-1):
    rev = rev + str[i]
print(rev) 
if (rev==str):
    print("It is a palindrome word")
else:
    print("It is not a palindrome word") 