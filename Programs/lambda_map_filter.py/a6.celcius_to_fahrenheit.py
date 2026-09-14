temp_in_celcius =[20,30,40,50]

temp_in_fahrenheit = list(map(lambda temp:9*temp/5+32,temp_in_celcius))
print(temp_in_fahrenheit)

print(list(filter(lambda n:n>100,temp_in_fahrenheit)))