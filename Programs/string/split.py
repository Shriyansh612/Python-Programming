# text = input("Enter string: ")
# text=text+" "
# length = len(text)
# word = ""
# print("[", end="")
# for i in range (0,length):
#     if(text[i]==" "):
#         print("\'"+word+"\'",end=",")
#         word=""
#     else:
#         word=word+text[i] 
# print("]")          


# ['my' , 'name' ]



#  new code

text = input ("Enter a string: ")   # my name is shriyuansh

words = []
word = ""

for ch in text:
    if ch != " ":   # white space
        word += ch
    else:
        if word != "":   # empty space
            words.append(word)
            word = ""

# add last word
if word != "":
    words.append(word)

print(words)
print(type(words))

# number = [1, 2, 3]
# number.append("4")

# print(number)

result = " ".join(words)
print(result)