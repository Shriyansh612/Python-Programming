# file = open("Programs//exception_handling//test.txt","r")
# total = 0 
# lines = file.readlines()
# print(lines)
# for line in lines:
#     try:
#         num = int(line.strip())
#         tatal += num
#     except Exception as err:
#         continue
# print(total)
# file.close()        


total = 0

with open("test.txt", "r") as file:
    for line in file:
        try:
            num = int(line.strip())
            total += num
        except Exception as err:
            continue
        
print("sum ",total )
