month = int(input(print("Enter month number: ")))
date = int(input(print("Enter date: ")))
day = 0
match month:
    case 1:
        day = date
    case 2:
        day = 31+date
    case 3:
        day = 31+28+date
    case 4:
        day = 31+28+31+date
    case 5:
        day = 31+28+31+30+date
    case 6:
        day = 31+28+31+30+31+date
    case 7:
        day = 31+28+31+30+31+30+date
    case 8:    
        day = 31+28+31+30+31+30+31+date
    case 9:    
        day = 31+28+31+30+31+30+31+31+date
    case 10:
        day = 31+28+31+30+31+30+31+31+30+date  
    case 11:      
        day = 31+28+31+30+31+30+31+31+30+31+date
    case 12:
        day = 31+28+31+30+31+30+31+31+30+31+30+date      
if (day%7==1):
    print("Thursday")
elif (day%7==2):
    print("Friday")
elif (day%7==3):
    print("Saturday")
elif (day%7==4):
    print("Sunday")
elif (day%7==5):
    print("Monday")
elif (day%7==6):
    print("Tuesday")
elif (day%7==0):
    print("Wednesday")                                                                   