def leap_year(n):
    if(n%400==0 or (n%4==0 and n%100!=0)):
        return True
    else:
        return False
    
years = [2020,2000,1900,2013,2026]

leap_years = list(filter(leap_year,years))
print(leap_years)