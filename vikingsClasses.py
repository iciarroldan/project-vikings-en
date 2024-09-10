import random

# Soldier
class Soldier: 
    def __init__(self, health, strength):   #function
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength  # access the soldier's strength

    def receiveDamage(self, damage):
        self.health -= damage  # remove the damage from health also it can be coded as: self.health = self.health - damage
    

# Viking

class Viking(Soldier): ## inherits from the soldier - attack 
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name #1st argument

    def battleCry(self):
        return "Odin Owns You All"

    def receiveDamage(self, damage): #needs to be reimplementes as the viking does different things than the soldier
        self.health -= damage
        if self.health > 0:
            return f"{self.health} has received {damage} points of damage" ## f' = function
        else:
            return f"{self.name} has died in act of combat" ## need to put a print so the messeage is printed out on the screen
        

# Saxon

class Saxon(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name 

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# how the war works

class War():
    def __init__(self): #constructor
        ##created 2 empty lists to start adding the soldiers to each list
        self.vikingArmy = [] 
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)  #adding vikings
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)   #adding saxons
    
    def vikingAttack(self):
        chosen_saxon = random.choice (self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        result = chosen_saxon.receiveDamage(chosen_viking.attack())
        #checking if the saxon is dead to remove it, there are 2 options: 
        #self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health < 0]
        if chosen_saxon.health <= 0:  
            self.saxonArmy.remove(chosen_saxon)
        return result

    def saxonAttack(self):
        chosen_saxon = random.choice (self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        result = chosen_viking.receiveDamage(chosen_saxon.attack())
        #checking if the saxon is dead to remove it, there are 2 options: 
        #self.vikingArmy = [viking for viking in self.vikingArmy if viking.health < 0]
        if chosen_viking.health <= 0:  
            self.vikingArmy.remove(chosen_viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day"
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass
