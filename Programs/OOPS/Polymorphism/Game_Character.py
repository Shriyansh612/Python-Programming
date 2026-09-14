class Character:
    def attack(self):
        pass
    
    def get_reward(self):
        pass
    
class Warrior(Character):
    def __init__(self):
        self.coins = 0

    def attack(self):
        print("Warrior Attacks") 

    def get_reward(self):
        self.coins = 100
        print("Reward: 100 Coins\n")  


class Mage(Character):
    def __init__(self):
        self.coins = 0

    def attack(self):
        print("Mage Attacks") 

    def get_reward(self):
        self.coins = 150
        print("Reward: 150 Coins\n")  


class Archer(Character):
    def __init__(self):
        self.coins = 0

    def attack(self):
        print("Archer Attacks") 

    def get_reward(self):
        self.coins = 120
        print("Reward: 120 Coins\n")  


class Assassin(Character):
    def __init__(self):
        self.coins = 0

    def attack(self):
        print("Assassin Attacks") 

    def get_reward(self):
        self.coins = 200
        print("Reward: 200 Coins\n")  
                                    

def defeat_enemy(character):
    character.attack()
    character.get_reward()

# characters = [Warrior(),Mage(),Archer(),Assassin()]    

# for ch in characters:
#     defeat_enemy(ch)


warrior = Warrior()
mage = Mage()
archer = Archer()
assassin = Assassin()


defeat_enemy(warrior)
print()

defeat_enemy(mage)
print()

defeat_enemy(archer)
print()

defeat_enemy(assassin)

