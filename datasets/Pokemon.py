import random
import datasets.constants as c
from .pokemontype import PokemonType
from .movement import Movement
from .targetype import *

class Pokemon:
    def __init__(self, name: str, level: int, health: float, attack: float, defense: float, speed: float, speattack: float, spedefense: float, typ1: PokemonType, typ2: PokemonType, movements):
        self.name = name
        self.level = level
        self.max_health = health
        self.health = health
        self.baseattack = attack
        self.basedefense = defense
        self.basespeed = speed
        self.basespeattack = speattack
        self.basespedefense = spedefense
        self.typ1 = typ1
        self.typ2 = typ2
        self.status = None

        self.attackbuff = 0
        self.defensebuff = 0
        self.speedbuff = 0
        self.speattackbuff = 0
        self.spedefensebuff = 0
        
        self.attack = self.baseattack * c.BUFF_MULTIPLIERS[self.attackbuff]
        self.defense = self.basedefense * c.BUFF_MULTIPLIERS[self.defensebuff]
        self.speed = self.basespeed * c.BUFF_MULTIPLIERS[self.speedbuff]
        self.speattack = self.basespeattack * c.BUFF_MULTIPLIERS[self.speattackbuff]
        self.spedefense = self.basespedefense * c.BUFF_MULTIPLIERS[self.spedefensebuff]
    
        self.movements = movements
        
        
    def recalculate_stats(self):
        
        """Recalculates every stat of a pokemon to apply new buffs
        
        Args:
            self: Instance of Pokemon
            
        Returns:
            None
            
        Comments:
            - Recalculates attack, defense, speattack, spedefense of a Pokemon
        """
        
        if self.attackbuff < -6:
            self.attackbuff = -6
        elif self.attackbuff > 6:
            self.attackbuff = 6
        
        if self.defensebuff < -6:
            self.defensebuff = -6
        elif self.defensebuff > 6:
            self.defensebuff = 6
            
        if self.speedbuff < -6:
            self.speedbuff = -6
        elif self.speedbuff > 6:
            self.speedbuff = 6
            
        if self.speattackbuff < -6:
            self.speattackbuff = -6
        elif self.speattackbuff > 6:
            self.speattackbuff = 6
            
        if self.spedefensebuff < -6:
            self.spedefensebuff = -6
        elif self.spedefensebuff > 6:
            self.spedefensebuff = 6
        
        
        self.attack = round(self.baseattack * c.BUFF_MULTIPLIERS[self.attackbuff], 2)
        self.defense = round(self.basedefense * c.BUFF_MULTIPLIERS[self.defensebuff], 2)
        self.speed = round(self.basespeed * c.BUFF_MULTIPLIERS[self.speedbuff], 2)
        self.speattack = round(self.basespeattack * c.BUFF_MULTIPLIERS[self.speattackbuff], 2)
        self.spedefense = round(self.basespedefense * c.BUFF_MULTIPLIERS[self.spedefensebuff], 2)
        
        
    def has_status(self) -> bool:
        
        """Checks wether a pokemon has a status
        
        Args:
            self: Instance of Pokemon

        Returns:
            bool: True if the pokemon has a status, False if not
        """
        
        return self.status != None    
        
        
    def is_alive(self) -> bool:
        
        """Checks wether a pokemon is alive
        
        Args:
            self: Instance of Pokemon

        Returns:
            bool: True if the pokemon is alive, False if not
        """
        
        return self.health > 0
    
    def print_pokemon_movements(self):
        
        """
        Prints every movement of a certain pokemon.
        
        Args:
            self: Instance of Pokemon
            
        Returns:
            None
        """
        
        for i, movement in enumerate(self.movements):
            if movement is not None:
                print(f"{i+1}. {movement.name}")
                
            else:
                print(f"{i+1}. No movement")
                
    def enter_valid_movement_selection(self):
        
        """
        When the user introduces a valid movement number, the choice gets returned as an integer

        Returns:
            int: The movement index of the movement that the user wants to select
        """
        
        chosen_movement_number = 0
        
        while True:
            try:
                chosen_movement_number = int(input("Enter your choice: "))
                
            except ValueError:
                print("Your choice is not a number.")
                
            if chosen_movement_number not in range(1, len(self.movements) + 1):
                print("The chosen number is too large or too small.")
            elif self.movements[chosen_movement_number - 1] is None:
                print("The pokemeon has not an available movement at the selected number.")
            else:
                print(f"{self.name} is going to use {self.movements[chosen_movement_number-1].name}")
                return chosen_movement_number - 1
        
    def use_movement(self, movement: Movement, enemy: "Pokemon"):
        print(f"{self.name} is trying to use {movement.name}")
        if self.has_movement(movement):
            print(f"{self.name} used {movement.name}.")
            
        else:
            print(f"{self.name} does not have {movement.name} in his movements.")
            return False
        
        self.set_target(movement, enemy)
        
        for effect in movement.effects:
            
            if effect["category"] == EffectCategory.STATCHANGE:
                effect = StatChangeEffect(self, enemy, effect["stat"], effect["magnitude"], effect["probability"], enemy if effect["target"]== TargetType.ENEMY else self)
                if effect.connected():
                    print(f"The actual {effect.stat} from {effect.target.name} is {effect.target.get_current_stat(effect.stat)}")
                    effect.target.modify_stat(effect.stat, effect.magnitude)
                else:
                    print("The effect did not connect.")
                    
            elif effect["category"] == EffectCategory.HEAL:
                effect = HealEffect(self, enemy, effect["heal_amount"], effect["probability"], enemy if effect["target"]== TargetType.ENEMY else self)
                if effect.connected():
                    print(f"{effect.target.name}'s health was {effect.target.health}")
                    effect.target.heal(effect.heal_amount)
                    print(f"{effect.target.name}'s health is now {effect.target.health}")
                else:
                    print("The effect did not connect.")
                
            elif effect["category"] == EffectCategory.STATUSEFFECT:
                effect = StatusEffect(self, enemy, effect["type"], effect["probability"], enemy if effect["target"]== TargetType.ENEMY else self)
                print("Using status effect.")
                if effect.target.has_status():
                    print("The pokemon already has a status.")
                    
                elif effect.connected():
                    effect.target.status = effect.type
                    print(f"{effect.target.name} was {effect.type}")
                    
                else:
                    print("The effect did not connect.")
                
            elif effect["category"] == EffectCategory.DAMAGE:
                print(effect)
                effect = DamageEffect(self, enemy, effect["probability"], movement, enemy if effect["target"]== TargetType.ENEMY else self)
                print(effect.user.name)
            
                if effect.connected():
                    dmg = ((((2 * effect.user.level * effect.user.critical()) / 5 + 2) * movement.power + 2) * effect.user.attack / effect.target.defense / 50) * effect.user.movement_stab(movement) * effect.user.extra_dmg_type(movement, effect.target) \
                    * random.randint(217, 255) // 255
                    effect.target.set_health(dmg)
                    print(f"The movement caused {dmg} on {effect.target.name}")

                
    def heal(self, amount):
        if self.health + amount < self.max_health:
            self.health += amount
            
        else:
            self.health = self.max_health
              
    def get_current_stat(self, stat):
        if stat == "attack":
            return self.attack
        
        elif stat == "defense":
            return self.defense
        
        elif stat == "speed":
            return self.speed
        
        elif stat == "speattack":
            return self.speattack
        
        elif stat == "spedefense":
            return self.spedefense
        
        else:
            print(f"The stat {stat} was not defined.")
             
    def modify_stat(self, stat, magnitude):
        if stat == "attack":
            self.attackbuff += magnitude
        elif stat == "defense":
            self.defensebuff += magnitude
        elif stat == "speed":
            self.speedbuff += magnitude
        elif stat == "speattack":
            self.speattackbuff += magnitude
        elif stat == "spedefense":
            self.spedefensebuff += magnitude   
        else:
            print(f"The stat {stat} is not defined")
        self.recalculate_stats()
        print(f"{self.name}'s {stat} was buffed and is now {self.get_current_stat(stat)}")
        
    def has_movement(self, movement: Movement):
        
        """
        Checks wether a pokemon has a movement

        Args:
            self: Instance of Pokemon
            movement (Movement): Instance of the movement that we want to check if a pokemon has
        
        Returns:
            bool: True if the pokemon has the movement, False if not
        """
        
        return movement in self.movements
        
    def attack_enemy(self, movement: Movement, target, chosen_target = None):
        #Calculates the amount of damage a movement will do

        if self.movement_connected(movement):
            if movement.power != 0:
                dmg = ((((2 * self.level * self.critical()) / 5 + 2) * movement.power + 2) * self.attack / target.defense / 50) * self.movement_stab(movement) * self.extra_dmg_type(movement, target) \
                * random.randint(217, 255) // 255
                print(f"The damage taken was {dmg}")
                target.set_health(dmg)
            else:
                pass
            
            movement.execute_effects(user=self, defender=target, chosen_target = chosen_target)
            if not target.is_alive():
                print(f"{target.name} is defeated")
                
            else:
                print(f"{target.name} remaining HP is {target.health}")
            
            
        else:
            print(f"{movement.name} did not connect")
            
            
    def set_health(self, damage_taken):
        
        #This function modifies the health of a pokemon whenever it takes damage
        
        self.health = max(0, self.health - damage_taken)
        
        
    def movement_connected(self, movement) -> bool:
        
        # This function returns True if a movement connected and False if it did not according to the precision of the movement
        
        threshold = random.random()
        return threshold < movement.accuracy / 100
    
    
    def movement_stab(self, movement) -> float:
        
        #Checks wether the movement's type is the same as some pokemon type
        
        if movement.typ == self.typ1 or movement.typ == self.typ2:
            stab = 1.5   
        else:
            stab = 1
            
        return stab
    
    
    def critical(self) -> int:
        
        #Checks wether a movement will critically strike
        
        threshold = self.speed / 512
        current = random.random()
        if current < threshold:
            print("It was a critical move")
            return 2
            
        else:
            return 1
        

    def extra_dmg_type(self, movement: Movement, enemy) -> float:
        
        """Returns the type effectiveness boost of a movement
        
        Args:
            - self: An instance of Pokemon
            - movement: The used movement
            - enemy(Pokemon): The enemy pokemon
            
        Returns:
            - float: The effectiveness boost
        
        Comments:
            - The effectiveness buff must be between 0 and 2
            - If it's 0 the movement does not affect the enemy's type
            - Informs the trainer of the effectiveness of the used attack
        
        """
        
        if enemy.typ1 in c.TABLETYPES[movement.typ][0]:
            boost_first_type = 2
        elif enemy.typ1 in c.TABLETYPES[movement.typ][1]:
            boost_first_type = 0.5  
        elif enemy.typ1 in c.TABLETYPES[movement.typ][2]:
            boost_first_type = 0
        else:
            boost_first_type = 1
                
        if enemy.typ2 == None:
            boost_second_type = 1
        elif enemy.typ2 in c.TABLETYPES[movement.typ][0]:
            boost_second_type = 2
        elif enemy.typ2 in c.TABLETYPES[movement.typ][1]:
            boost_second_type = 0.5
        elif enemy.typ2 in c.TABLETYPES[movement.typ][2]:
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
    
    
    def set_target(self, movement:"Movement", enemy:"Pokemon"):
        if movement.default_target == "OWN":
            target = self
            
        else:
            target = enemy
            
        return target