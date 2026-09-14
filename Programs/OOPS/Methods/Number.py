class number:

    count = 0

    def __init__(self,n):
        self.n = n
        number.count += 1

    #function to print the second highest unique digit
    def second_unique(self):#16
        self.n = str(self.n)        
        count = []
        for i in range(0,10):
            count.append(self.n.count(str(i)))
        count.sort()    
        print(count[-2])

    #whether all digits are unique are not #17
    def unique_digits(self):
        self.n = str(self.n)
        for i in range(10):
            if(self.n.count(str(i))>1):
                return False 
        return True       

    #longest consecutive sequence of same digit #18
    def longest_sequence(self):
        self.n = str(self.n) 
        longest = 0
        longest_digit = 0
        for i in range(len(self.n)):
            for j in range(i,len(self.n)):
                for k in range(0,10):
                    if (self.n[i:j+1]==str(k)*(j+1-i)):
                        if((j+1-i)>longest):
                            longest = j+1-i
                            longest_digit = self.n[i]
        print("Longest occuring sequence is of",longest_digit,"of",longest,"digits long")


    #divide number into two equal halves and check whether they have equal sum of digits #19
    def divide_number(self):
        if (len(str(self.n))%2!=0):
            print("Such a split is not possible")                                   
        else:
            sum1 = 0
            sum2 = 0 
            l = len(str(self.n))
            while (self.n!=0):
                if (len(str(self.n))>l/2):
                    sum1+=self.n%10
                else:
                    sum2+=self.n%10
                self.n=self.n//10

            # print(sum1,sum2)                

            if(sum1==sum2):
                print("equal")                
            else:
                print("Not equal")
     
    #smallest digit that occurs only once in the number  #20               
    def smallest_only_once(self):
        self.n = str(self.n)
        smallest = 9
        for i in range(10):
            if (self.n.count(str(i))==1):
                if (i<smallest):
                    smallest = i
        print("Smallest digit that occurs only once:",smallest)

    @classmethod
    def count_object(cls):
        print(cls.count)                    


obj1 = number(1232342)
# obj1.second_unique()     

obj2 = number(1111122333)
# obj2.longest_sequence()

obj3 = number(12334448712)
# obj3.smallest_only_once()

# number.count_object()
obj4 = number(3113)
obj4.divide_number()