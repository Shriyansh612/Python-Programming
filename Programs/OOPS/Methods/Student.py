class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        # self.maths = maths
        # self.phy = phy
        # self.chem = chem

    # def average(self):
    #     average = (self.maths+self.phy+self.chem)/3
    #     return(average)'

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is : ", sum/3)

s1 = Student("Tony stark", [99, 98, 97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()


# s1 = Student("Shriyansh",70,80,90)

# print("Average marks of all 3 subjects:",s1.average())