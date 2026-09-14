import random
a = random.randint(1,100)
c = 1
print('''
       NUMBER GUESSING GAME

You have to guess a number between 
1 to 100 in 7 chances

You would be provided information 
about your number being larger or 
smaller than the true number, on 
the basis of which you have to make
a guess.          
''')
while(c<=7):
    n = int(input(""))
    if (n<a):
        print("Your number is smaller")
    elif (n>a):
        print("Your number is larger")
    else:
        print("Victory")
        break
    c+=1
    if(c==8):
        print("Game Over")
        break        
