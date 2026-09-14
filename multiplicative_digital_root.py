n = int(input("Enter a number: "))
def multiplicative_digital_root(num):
    multiplicative_persistance = 0
    while(num>10):
        product = 1
        while(num!=0):
            product=product*(num%10)
            num=num//10
        num = product
        multiplicative_persistance+=1
    return num,multiplicative_persistance

mdr, mp = multiplicative_digital_root(n)
print(f"Multiplicative digital Root: {mdr}\nMultiplicative Persistance: {mp}")    

