try:
    list1 = list(map(int,input().split()))
    list2 = list(map(int,input().split()))
    if (len(list1)!=len(list2)):
        raise err1
    result = []
    for i in range(len(list1)):
        result.append(list1[i]/list2[i])
    print(result)       
except ZeroDivisionError:
    print("Division by zero is not allowed")
except Exception as err1:
    print("Please enter lists of equal lengths")     