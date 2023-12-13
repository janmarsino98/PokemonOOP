import random
from datasets.constants import TABLETYPES

class Pokemon:
    def __init__(self, name, level, health, attack, defense, speed, speattack, spedefense, typ1, typ2, movements):
        self.name = name
        self.level = level
        self.health = health
        self.baseattack = attack
        self.basedefense = defense
        self.basespeed = speed
        self.basespeattack = speattack
        self.basespedefense = spedefense
        self.typ1 = typ1
        self.typ2 = typ2

        self.attackbuff = 0
        self.defensebuff = 0
        self.speedbuff = 0
        self.speattackbuff = 0
        self.spedefensebuff = 0
        
        self.attack = self.baseattack * (1 + self.attackbuff * 0.5)
        self.defense = self.basedefense * (1 + self.defensebuff * 0.5)
        self.speed = self.basespeed * (1 + self.speedbuff * 0.5)
        self.speattack = self.basespeattack * (1 + self.speattackbuff * 0.5)
        self.spedefense = self.basespedefense * (1 + self.spedefensebuff * 0.5)
    
        self.movements = movements
        
    def is_alive(self):
        return self.health > 0
    
    def select_movement(self):
        chosen = 0
        while chosen not in [1,2,3,4]:
            chosen = int(input(f"Please select a valid movement:\n1.{self.movements[0].name}\n2.{self.movements[1].name}\n3.{self.movements[2].name}\n4.{self.movements[3].name}\n"))
        print(f"Your chosen attack is {self.movements[chosen-1].name}")
        return self.movements[chosen-1]
        
    def attack_enemy(self, movement, enemy):
        if self.movement_connected(movement):
            dmg = (((2*self.level*self.critical())/5+2)*movement.power * self.attack / enemy.defense / 50 + 2) * self.movement_stab(movement) * self.extra_dmg_type(movement, enemy) \
            * random.randint(217, 255)//255
            enemy.set_health(dmg)
            if not enemy.is_alive():
                print(f"{enemy.name} is defeated")
                
            else:
                print(f"{enemy.name} remaining HP is {enemy.health}")
            
            
        else:
            print("The movement did not connect")
            
            
    def set_health(self, damage_taken):
        self.health = max(0, self.health - damage_taken)
        
        
    def movement_connected(self, movement):
        
        # This function returns True if a movement connected and False if it did not according to the precision of the movement
        
        threshold = random.random()
        return threshold < movement.precision / 100
    
    def movement_stab(self, movement):
        if movement.typ == self.typ1 or movement.typ == self.typ2:
            stab = 1.5
            
        else:
            stab = 1
            
        return stab
    
    def critical(self):
        threshold = self.speed / 2
        current = random.random() * 100
        if current < threshold:
            return 2
        else:
            return 1
        
    def extra_dmg_type(self, movement, enemy):
        if enemy.typ1 in TABLETYPES[movement.typ][0]:
            boost_first_type = 2
        elif enemy.typ1 in TABLETYPES[movement.typ][1]:
            boost_first_type = 0.5  
        elif enemy.typ1 in TABLETYPES[movement.typ][2]:
            boost_first_type = 0
        else:
            boost_first_type = 1
                
        if enemy.typ2 == None:
            boost_second_type = 1
        elif enemy.typ2 in TABLETYPES[movement.typ][0]:
            boost_second_type = 2
        elif enemy.typ2 in TABLETYPES[movement.typ][1]:
            boost_second_type = 0.5
        elif enemy.typ2 in TABLETYPES[movement.typ][2]:
            boost_second_type = 0
        else:
            boost_second_type = 1
            
        extra_dmg = boost_first_type * boost_second_type
        
        if extra_dmg == 4:
            print("The attack is supereffective")
            
        elif extra_dmg == 2:
            print("The attack is very effective")
        
        elif extra_dmg == 0.5:
            print("The attack is not very effective")
        
        elif extra_dmg == 0.25:
            print("The attack is supperineffective")
            
        elif extra_dmg == 0:
            print("The attack does not affect the enemy")
        
            
        return boost_first_type * boost_second_type