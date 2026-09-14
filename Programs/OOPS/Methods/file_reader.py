class PDFFile:
    def __init__(self):
        self.file = open("test.pdf","r+")

    def file_processor(self):
        data = self.file.read()
        print(data)

class TextFile:
    def __init__(self):
        self.file = open("test2.txt","r+")

    def file_processor(self):
        data = self.file.read()
        print(data)

class PyFile:
    def __init__(self):
        self.file = open("try.py","a+")

    def file_write(self):
        while(True):
            line = input()
            if (line=="STOP"):
                break
            else:
                self.file.write(line+"\n")


    def file_processor(self):
        data = self.file.read()        
        print(data)

# pdf1 = PDFFile()        
# txt1 = TextFile()
py1 = PyFile()

# pdf1.file_processor()
# txt1.file_processor()
py1.file_write()

