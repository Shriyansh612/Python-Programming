list = ["cat","dog","apple","car","banana"]

dict = {}

for i in list:
    length = len(i)
    if length not in dict:
        dict.update({length:[]})
    dict[length].append(i)


for key,value in dict.items():
    print(key,":",value)