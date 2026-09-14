class MathOperation:

    count = 0
    def __init__(self,n):
        self.n = n
        MathOperation.count+=1
        

    #instance method
    def add(self,b):
        self.n += b

    #static method
    @staticmethod
    def prime(a):
        c = 0
        for i in range(1,a+1):
            if (a%i==0):
                c+=1
        if (c==2):
            return True
        else:
            return False

    #class method
    @classmethod
    def print_count(cls):
        print("No. of objects created =",cls.count)

obj1 = MathOperation(5)        
obj2 = MathOperation(8)
obj3 = MathOperation(1)
obj4 = MathOperation(10)

obj1.add(2)
print(MathOperation.prime(11))
MathOperation.print_count()
print(obj1.n)