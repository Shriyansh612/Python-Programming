from abc import ABC, abstractmethod

class Notification:
    @abstractmethod
    def send(self,message):
        pass

class EmailNotification(Notification):
    def send(self,message):
        print(message)    

class SMSNotification(Notification):
    def send(self,message):
        print(message)

class PushNotification(Notification):
    def send(self,message):
        print(message)

not1 = EmailNotification()                        
not2 = SMSNotification()
not3 = PushNotification()

not1.send("Email received")
not2.send("SMS Received")
not3.send("Push Notification received")