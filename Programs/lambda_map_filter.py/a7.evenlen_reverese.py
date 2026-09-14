words=["hello","hi","bye","good"]

filtered_words = list(filter(lambda word:len(word)%2==0,words))
print(filtered_words)

print(list(map(lambda word:word[::-1],filtered_words)))