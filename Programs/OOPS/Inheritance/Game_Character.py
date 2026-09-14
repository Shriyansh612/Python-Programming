import random
class Game_Character:
    def __init__(self,name):
        self.name = name

class Warrior(Game_Character):
    def __init__(self,name):
        self.passive = False
        self.defeated = False   
        super().__init__(name)

class Knight(Warrior):

    def __init__(self):
        name = input("Enter character name: ")       
        super().__init__(name)
        self.hp = 100
        self.heal_potion = 2

    def attack(self,obj):
        damage = random.randint(0,100)        
        obj.hp = obj.hp - damage
        if (obj.hp<0):
            obj.hp = 0
            obj.defeated = True
            print(obj.name, "is defeated!!")

    def heal(self):
        if (self.heal_potion>0):
            heal_hp = random.randint(0,100)        
            self.hp = self.hp + heal_hp
            self.heal_potion-=1
            if (self.hp >100):
                self.hp = 100
        else:
            print("All Healing Potions are used")
                 

print ("Player 1:")
p1 = Knight()     
print ("Player 1 created\n")            

print ("Player 2:")
p2 = Knight()
print ("Player 2 created\n")


while (p1.defeated==False and p2.defeated==False):
    print ("\nPlayer 1's Turn: ")
    print ("To Attack: 1")
    print ("To Heal: 2\n")
    op = int(input())
    if (op==1):
        p1.attack(p2)
        print("\nPlayer 1:",p1.hp)
        print("Player 2:",p2.hp)

    elif (op==2):
        p1.heal()
        print("\nPlayer 1:",p1.hp)
        print("Player 2:",p2.hp)
    else:
        print("Wrong Operation")            

    
    if (p2.defeated==False):
        print ("Player 2's Turn: ")
        print ("To Attack: 1")
        print ("To Heal: 2\n")
        op = int(input())
        if (op==1):
            p2.attack(p1)
            print("\nPlayer 1:",p1.hp)
            print("Player 2:",p2.hp)
        elif (op==2):
            p2.heal()
            print("\nPlayer 1:",p1.hp)
            print("Player 2:",p2.hp)
        else:
            print("Wrong Operation")   

