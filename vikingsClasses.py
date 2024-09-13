import random

# Dictionary of weapons and their damage
weapons = {
    "Sword": 10,
    "Axe": 12,
    "Spear": 8,
    "Bow": 7,
    "Mace": 11
}

# Soldier
class Soldier: 
    def __init__(self, health, strength):   
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength  # returns the soldier's strength

    def receiveDamage(self, damage):
        self.health -= damage  # reduces health by the damage amount
    

# Viking

class Viking(Soldier):  # inherits from Soldier
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name  # first argument
        self.weapon = random.choice(list(weapons.keys()))  # Assign a random weapon
        self.weapon_damage = weapons[self.weapon]  # Get the damage associated with the weapon

    def attack(self):
        # The attack now includes the soldier's strength plus the weapon's damage
        return self.strength + self.weapon_damage

    def battleCry(self):
        return "Odin Owns You All"

    def receiveDamage(self, damage):  # reimplementation for Viking-specific behavior
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        

# Saxon

class Saxon(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name 
        self.weapon = random.choice(list(weapons.keys()))  # Assign a random weapon
        self.weapon_damage = weapons[self.weapon]  # Get the damage associated with the weapon

    def attack(self):
        # The attack now includes the soldier's strength plus the weapon's damage
        return self.strength + self.weapon_damage

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War mechanics

class War():
    def __init__(self):  # constructor
        # Create two empty lists to store soldiers in each army
        self.vikingArmy = [] 
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)  # Add a viking to the Viking army
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)  # Add a saxon to the Saxon army
    
    def vikingAttack(self):
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        result = chosen_saxon.receiveDamage(chosen_viking.attack())
        if chosen_saxon.health <= 0:  
            self.saxonArmy.remove(chosen_saxon)  # Remove dead Saxon from the army
        return result

    def saxonAttack(self):
        chosen_saxon = random.choice(self.saxonArmy)
        chosen_viking = random.choice(self.vikingArmy)
        result = chosen_viking.receiveDamage(chosen_saxon.attack())
        if chosen_viking.health <= 0:  
            self.vikingArmy.remove(chosen_viking)  # Remove dead Viking from the army
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day"
        else:
            return "Vikings and Saxons are still in the thick of battle."