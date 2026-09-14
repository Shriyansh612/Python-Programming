data = [1,"4","4.3",3.14,True,"hello"]
for i in range(len(data)):
    try:
        data[i] = int(data[i])
    except Exception as err:
        continue    

print(data)