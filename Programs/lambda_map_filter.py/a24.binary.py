def check(n):
    binary = bin(n)[2:]
    if(binary.count("1")>3):
        return True
    else:
        return False
    
numbers = [7,15,31,33,14,30]

print(list(filter(check,numbers)))