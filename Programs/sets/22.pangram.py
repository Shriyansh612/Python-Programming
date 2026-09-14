text = input("Enter text: ").lower()

missing_letters = set()
unique = set()
duplicate = set()

for i in range(97,123):
    count = text.count(chr(i))
    if (count==0):
        missing_letters.add(chr(i))
    elif (count==1):
        unique.add(chr(i))
    elif (count>1):
        duplicate.add(chr(i))

print("Missing Letters:",sorted(missing_letters))
print("Duplicate Letters:",sorted(duplicate))
print("Unique Letters:",sorted(unique))
