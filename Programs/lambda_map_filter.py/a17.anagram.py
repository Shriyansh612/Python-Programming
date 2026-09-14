words = ["hello","oellh","olleh","computer","hands"]
given_word = "hello"

def alphabetical(word):
    result=""
    for i in range(0,256):
        for j in range(0,len(word)):
            if(word[j]==chr(i)):
                result=result+chr(i)
    return result

print(list(filter(lambda word:word if alphabetical(word)==alphabetical(given_word) else None,words)))                