text = input("Enter a string: ")
# l = len(text)
count = 1
result=""
for i in range(1, len(text)):
    if (text[i]==text[i - 1]):
            count+=1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)
print(result)
    