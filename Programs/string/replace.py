text = input("Enter string: ")
to_replace = input("Enter string to be replaced: ")
replace_with = input("Enter string by which it is to be replaced: ")\

result = ""
# str = ""
i=0
l = len(to_replace) 
if (not to_replace in text):
    print("To be replaced string must be present in original string")
else:
    # while(i<len(text)-l+1):
    #     str = text[i:i+l]
    #     if (str==to_replace):
    #         result = result+replace_with
    #         i=i+l
    #     else:
    #         if(text[-(l-1):]==str):
    #             result=result+text[i:]
    #         else:    
    #             result+=text[i]
    #         i += 1 

        while i < len(text):

            if text[i:i+l] == to_replace:
                 result = result + replace_with
                 i += l
            else:
                result += text[i]
                i +=1

            
# if (l>1):
#     result=result+text[-(l-1):]
print(result)            
