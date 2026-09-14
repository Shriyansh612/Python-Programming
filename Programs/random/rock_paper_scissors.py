import random
n = 1
while(n==1):
    choice = input("Rock, Paper, Scissors: ")
    match choice:
        case "R":
            a = random.randint(1,3)
            if (a==1):
                print("Rock")
            elif (a==2):
                print("Paper")
                print("You Lose")
                n = 2
            else:
                print("Scissors")
                print("You Win")
                n = 2 
        case "S":
            a = random.randint(1,3)
            if (a==1):
                print("Scissors")
            elif (a==2):
                print("Rock")
                print("You Lose")
                n = 2
            else:
                print("Paper")
                print("You Win")
                n=2
        case "P":
            a = random.randint(1,3)
            if (a==1):
                print("Paper")
            elif (a==2):
                print("Scissors")
                print("You Lose")
                n = 2
            else:
                print("Rock")
                print("You Win")
                n=2           
        case "":
            print("Invalid Input")     
                           