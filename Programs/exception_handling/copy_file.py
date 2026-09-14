try:
    file1 = open(input("Enter file to copy: ")+".txt","r")
    file2 = open(input("Enter file to paste: ")+".txt","r+")
    data = file1.read()
    file2.write(data)
    file1.close()
    file2.close()
except Exception as err:
    print("Error")    