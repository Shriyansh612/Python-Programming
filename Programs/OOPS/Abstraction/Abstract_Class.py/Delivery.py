from abc import ABC, abstractmethod
class Delivery:
    def __init__(self):
        delivery_id = int(input("Enter delivery id: "))
        distance = int(input("Enter distance of delivery: "))
        base_charge = int(input("Enter base_charge: "))
        self.delivery_id = delivery_id
        self.distance = distance
        self.base_charge = base_charge

    @abstractmethod
    def calculate_charge(self):
        pass

class BikeDelivery(Delivery):            
    def __init__(self):
        super().__init__()
    def calculate_charge(self):
        print("Bill:",self.base_charge+20*self.distance)

class CarDelivery(Delivery):            
    def __init__(self):
        super().__init__()
    def calculate_charge(self):
        print("Bill:",self.base_charge+60*self.distance)

class TruckDelivery(Delivery):            
    def __init__(self):
        super().__init__()
    def calculate_charge(self):
        print("Bill:",self.base_charge+100*self.distance)

del1 = BikeDelivery()
del1.calculate_charge()

del2 = CarDelivery()
del2.calculate_charge()

del3 = TruckDelivery()
del3.calculate_charge()



