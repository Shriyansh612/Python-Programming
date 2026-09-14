# text = [" My name is Shriyansh","I love Python","Python is an easy language"]

n = int(input("How many sentences ? "))

max_word = 0
max_sentence=""

for i in range(n):
    sentence = input("Enter sentence: ")

    word_count = len(sentence.split())

    if word_count > max_word:
        max_word = word_count
        max_sentence = sentence

print("Maximium number of words :", max_word)
print(max_sentence)