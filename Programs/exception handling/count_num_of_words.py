try:
    file_name = input("Enter file name: ")+".txt"
    file = open(file_name,"r")
    n = 0
    lines = file.readlines()
    for line in lines:
        line.strip()
        words = line.split()
        words = list(map(lambda word : word.strip(),words))
        n += len(words)
except FileNotFoundError:
    print("No file exists by such name")
else:
    print("Number of words:",n)                