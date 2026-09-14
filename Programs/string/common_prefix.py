strs = ["dog","racecar","car"]
common_prefix = "" 
smallest_word_length = min(len(strs[0]),len(strs[1]),len(strs[2]))
for i in range (0,smallest_word_length):
    if (strs[0][0:i+1]==strs[1][0:i+1]==strs[2][0:i+1]):
        common_prefix = strs[0][0:i+1]
    else:
        break
print("Common Prefix: ", common_prefix)
if (common_prefix==""):
    print("There is no common prefix among the input strings.")        