class Weapon:
    def use(self):
        pass

class Sword(Weapon):
    def use(self):
        print("Sword Attack!")    

class Bow(Weapon):
    def use(self):
        print("Arrow Fired!")        

class MagicWand(Weapon):
    def use(self):
        print("Magic Spell!")

class Shield(Weapon):
    def use(self):
        print("Shield Activated!")                

objects = [Sword(),Bow(),MagicWand(),Shield()]        

for obj in objects:
    obj.use()
    print()