num = []
try:
    for i in range(5):
        num.append(int(input()))
    print("Maximum:",max(num))  
except Exception as err:
    print("Only integer values are allowed")      