from abc import ABC, abstractmethod

class Patient:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    @abstractmethod
    def calculate_bill(self,days):
        pass
class General_Patient(Patient):
    def __init__(self,name,id):
        super().__init__(name,id)             

    def calculate_bill(self,days):
        print("Bill:",2000*days)        
        
class Emergency_Patient(Patient):
    def __init__(self,name,id):
        super().__init__(name,id)             

    def calculate_bill(self,days):
        print("Bill:",5000*days)

class ICU_Patient(Patient):
    def __init__(self,name,id):
        super().__init__(name,id)             

    def calculate_bill(self,days):
        print("Bill:",10000*days)    


patient1 = General_Patient("shriyansh",101)            
patient2 = Emergency_Patient("raghu",103)            
patient3 = ICU_Patient("ravi",102)            

patient1.calculate_bill(5)
patient2.calculate_bill(5)
patient3.calculate_bill(5)
