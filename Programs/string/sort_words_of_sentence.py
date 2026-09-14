text = input("Enter a string: ")

#Shortest to Longest

words = text.split()
# words1 = words

for i in range (len(words)-1,0,-1):
    for j in range (0,i):
        assign = ""
        if (len(words[j])>len(words[j+1])):
            assign = words[j]
            words[j] = words[j+1]
            words[j+1] = assign
            
print(" ".join(words))

print(" ".join(words[::-1]))


#alphabetically

# for i in range (len(words1)-1,0,-1):
    # for j in range (0,i):
