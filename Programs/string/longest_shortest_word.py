# str = input('Enter a string: ')
# words = str.split()
# long = ""
# d = 0
# for i in range(0,len(words)):
#     l=len(words[i])
#     if(l>d):
#         d=l
#         long = words[i]
#     print (words[i],":",l)
# print("Longest Word is:", long)

sentence = input("Entter the value : ")
words = sentence.split()
longest_word = ""
shortest_word = " "*(len(sentence)+1)
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) < len(shortest_word):
        shortest_word = word
    print( word, len(word))
print("Longest word : ", longest_word)
print("Shortest word : ", shortest_word)