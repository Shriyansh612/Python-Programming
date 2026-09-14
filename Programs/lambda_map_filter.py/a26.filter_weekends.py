def weekend(date):
    d,m,y=int(date.split("-")[0]),int(date.split("-")[1]),int(date.split("-")[2])
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
    if(day%7==1 or day%7==2):
        return True
    else:
        return False

dates = ["27-06-2026","28-06-2026","29-06-2026","30-06-2026","29-07-2007"]

print(list(filter(weekend,dates)))