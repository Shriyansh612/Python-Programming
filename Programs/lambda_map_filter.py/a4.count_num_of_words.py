sentences = ["I love python","I am doing programming","i am eighteen years old"]

print(list(map(lambda sentence:[sentence,len(sentence.split())],sentences)))