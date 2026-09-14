y = int(input(print("Enter year: ")))
m = int(input(print("Enter month number: ")))
d = int(input(print("Enter date: ")))
day = 0
feb = 0
nl = 0
if(y%400==0 or (y%4==0 and y%100!=0)):
    feb = 29
else:
    feb = 28
for i in range(2000,y): 
    if(i%400==0 or (i%4==0 and i%100!=0)):
        nl+=1
day = 365*((y-2000)-nl) + 366*nl
print(nl)           
match m:
    case 1:
        day = d+day
    case 2:
        day = 31+d+day
    case 3:
        day = 31+feb+d+day
    case 4:
        day = 31+feb+31+d+day
    case 5:
        day = 31+feb+31+30+d+day
    case 6:
        day = 31+feb+31+30+31+d+day
    case 7:
        day = 31+feb+31+30+31+30+d+day
    case 8:    
        day = 31+feb+31+30+31+30+31+d+day
    case 9:    
        day = 31+feb+31+30+31+30+31+31+d+day
    case 10:
        day = 31+feb+31+30+31+30+31+31+30+d+day 
    case 11:      
        day = 31+feb+31+30+31+30+31+31+30+31+d+day
    case 12:
        day = 31+feb+31+30+31+30+31+31+30+31+30+d+day
print(day)             
if (day%7==1):
    print("Saturday")
elif (day%7==2):
    print("Sunday")
elif (day%7==3):
    print("Monday")
elif (day%7==4):
    print("Tuesday")
elif (day%7==5):
    print("Wednesday")
elif (day%7==6):
    print("Thursday")
elif (day%7==0):
    print("Friday")                                                                   