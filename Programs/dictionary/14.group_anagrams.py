# def anagram(str1,str2):
#     new_str1=""
#     new_str2=""
#     for i in range(256):
#         if chr(i) in str1 :
#             new_str1+=chr(i)*str1.count(chr(i))
#         if chr(i) in str2 :
#             new_str2+=chr(i)*str2.count(chr(i))
#     return new_str1==new_str2

# def alphabetically(word):
#     alpha = ""
#     for i in range(65,91):
#         if(chr(i) in word or chr(i+32) in word):
#             alpha += chr(i+32)*word.count(chr(i+32)) + chr(i)*word.count(chr(i))
#     return alpha   

# words = ["eat","tea","tan","ate","nat","bat"]
# result = {}
# for i in range(len(words)):
#     if(alphabetically(words[i]) in result):
#         continue
#     value = [words[i]]
#     for j in range (i+1,len(words)):
#         if(anagram(words[i],words[j])):
#             value.append(words[j])
#     result.update({alphabetically(words[i]) : value})

# for key,value in result.items():
#     print(key,":",value)


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = {}

for word in words:
    key = "".join(sorted(word))  # sort letters to create a common key

    if key not in result:
        result[key] = []

    result[key].append(word)

for key,value in result.items():
    print(key,":",value)