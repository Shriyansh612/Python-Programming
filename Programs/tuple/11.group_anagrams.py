def anagram(str1,str2):
    new_str1=""
    new_str2=""
    for i in range(256):
        if chr(i) in str1 :
            new_str1+=chr(i)*str1.count(chr(i))
        if chr(i) in str2 :
            new_str2+=chr(i)*str2.count(chr(i))
    # if(new_str1==new_str2):
    #     return True
    # else:
    #     return False

    return new_str1 == new_str2

# list = list(input().split())
# result = []

# for i in range(len(list)):
#     result.append(list[i])
#     for j in range(i+1,len(list)):
#         if(anagram(list[i],list[j]) and (list[j] not in result)):
#             # list.remove(list[j])
#             result.append(list[j])

# print(result)           


# tup = tuple(input("Enter the words : ").split())

# visited = ()

# for i in range(len(tup)):

#     if tup[i] in visited:
#         continue

#     print(tup[i], end=" ")
#     visited += (tup[i],)

#     for j in range(i + 1, len(tup)):

#         if anagram(tup[i], tup[j]):
#             print(tup[j], end=" ")
#             visited += (tup[j],)
        
#     print()
