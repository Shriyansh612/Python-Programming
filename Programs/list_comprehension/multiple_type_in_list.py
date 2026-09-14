list = ["hello",1,3.14,True,"123"]

result = [val for val in list if isinstance(val,str)]
print(result)