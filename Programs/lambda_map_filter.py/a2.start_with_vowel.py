words = ["even","one","world","computer","electronics"]

filtered_words = list(filter(lambda word : word[0] in 'aeiou',words))
print(filtered_words)

print(list(map(lambda word:word.capitalize(),filtered_words)))