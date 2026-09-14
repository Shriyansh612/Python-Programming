try:
    file_name = input("Enter file name: ")
    file = open(file_name+".txt","r")
    print("No. of words:",len(file.read().split()))
except FileNotFoundError:
    print("File does not exist")    