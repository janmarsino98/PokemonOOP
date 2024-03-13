from random import random
from datasets.pokemontype import PokemonType
import datasets.constants as c
from .targetype import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datasets.pokemon import Pokemon

class Movement:
    def __init__(self, name: str, power: int, pp: int, accuracy: float, typ: PokemonType, effects: list[Effect], default_target:TargetType):
        self.name = name
        self.power = power
        self.pp = pp
        self.accuracy = accuracy
        self.typ = typ
        self.effects = effects
        self.target = None
        self.default_target = default_target
    
    def connected(self) -> bool:
        """
        Decides if a movement connected or failed
        
        Args:
            self(Movement): The Movement instance
            
        Returns:
            bool
            True if connected
            False if failed
    
        """    

        threshold = random.random()
        return threshold < self.accuracy / 100
            
    def calculate_movement_damage(self, user: "Pokemon", target:"Pokemon") -> int:
        
        """Calculates the amount of damage a certain movement will do

        Args:
            self: Instance of Movement
            user(Pokemon): Pokemon that is using the movement
            target(Pokemon): Pokemon that receives the movement
             
        Returns:
            int: Amount of damage dealt
        """
               
        if self.power != 0:
            damage = int(((((2 * user.level * self.critical(user)) / 5 + 2) * self.power + 2) * user.attack / target.defense / 50) * self.movement_stab(user) * user.extra_dmg_type(self, target) \
                    * random.randint(217, 255) / 255)
            return damage
        
        else:
            return 0
        
    def apply_damage(self, target: "Pokemon", damage: int):
        
        """Applies a given amount of damage to a target.
        
        Args:
            self: Instance of Movement
            target(Pokemon): Pokemon that will get it's health changed.
            damage(int): Amount that will be reduced (if positive) or increased (if negative).
            
        Returns:
            None
            
        Comments:
            - Informs the user of the new health of the target.
        """
        
        target.set_health(damage)
        print(f"{target.name} received {damage} damage. It now has {target.health} hps.")
        
    def calculate_and_apply_damage(self, user: "Pokemon", target: "Pokemon"):
        
        """Calculates the amount of damage that a movement would strike and applies it to the target
        
        Args:
            self: Instance of Movement
            user(Pokemon): Pokemon that uses the movement
            target(Pokemon): Pokemon taht receives the movement
            
        Returns:
            None
        """
        
        damage = self.calculate_movement_damage(user, target)
        if damage != 0:
            self.apply_damage(target, damage)

    def movement_stab(self, user: "Pokemon") -> float:
    
        """
        Checks if the movement type is the same as one of the user types. If it is, the damage of the move increases
        
        Args:
            self(Movement): The movement instance
            user(Pokemon): The Pokemon that uses the movement
            
        Returns:
            float
            1 if there is no stab
            1.5 if there is stab
            
        Notes:
            - The return numbers are then used in the deal_dmg formula to calculate a Movement damage
        """

        if self.typ == user.typ1 or self.typ == user.typ2:
            stab = 1.5
        else:
            stab = 1
            
        return stab

    
    def critical(self, user: "Pokemon") -> int:
    
        """
        Calculates wether a movement scored a critical move or not
        
        Args:
            self(Movement): The Movement instance
            user(Pokemon): The pokemon that used the movement
            
        Returns:
            1 if no criticial
            2 if critical
            
        Notes:
            - Returns one of theese numbers to use them  in the deal_dmg() formula
    
        """

        threshold = user.speed / 512
        current = random.random()
        if current < threshold:
            print("It was a critical move")
            return 2
            
        else:
            return 1
        
        
    def execute_movement_effects(self):
        for effect in self.effects:
            if effect.connected():
                if effect.category == EffectCategory.STATCHANGE:
                    effect = StatChangeEffect("")
        
        
       
    """def execute_effects(self):
        
        if self.effects is None:
            pass
        
        else:
            for effect in self.effects:
                
                if effect["category"] == EffectCategory.PRIORITY:
                    print("The movement will hit first")
                
                
                else:
                    effect_target = None
                    
                    if effect["target"] == TargetType.OWN:
                        
                        #If the TargetType is OWN the user will receive the effect
                        
                        effect_target = self.user
                    
                    elif effect["target"] == TargetType.ENEMY:
                        
                        #If the TargetType is ENEMY the defender will receive the effect
                        
                        target = defender
                    
                    elif effect["target"] == TargetType.CHOOSE:
                        
                        #If the TargetType is CHOOSE the target that the trainer selected will recieve the effect
                        
                        target = chosen_target
                
                    #STAT BUFF/NERF MOVEMENTS    
                    
                    if effect["category"] == EffectCategory.STATCHANGE:
                        self.executeStatChange(stat=effect["stat"], target=target, magnitude=effect["magnitude"])
                        
                        
                    #STATUS MOVEMENTS
                        
                    elif effect["category"] == EffectCategory.STATUSEFFECT:
                        
                        self.executeStatusEffect(target=target, effectAccuracy=effect["probability"], effectType=effect["type"])
                        
                    #HEALTH MOVEMENTS
                    
                    elif effect["category"] == EffectCategory.HEAL:
                        self.executeHealEffect(user=user, amount_to_heal=user.dmg/2)"""
                        
    
    def executeHealEffect(self, user, amount_to_heal):
        user.set_health(amount_to_heal)
        if amount_to_heal != 0:
            print(f"{user.name} healed {amount_to_heal} hp's.")

                
    def executeStatChange(self, stat: str, target, magnitude: float):
        
        """
        Modifies a Pokemon's stat when a movement is used
        
        Args:
            self(Movement): The Movement instance
            stat(str): The stat that needs to be modified
            target(Pokemon): The Pokemon that will undergo the stat modification
            magnitude(float): The amount by which the stat will be modified (can be positive or negative)
            
        Returns:
            None
            
        Comments:
            - Depending on the 'stat' parameter the function modifies the corresponding stat of the 'target' Pokemon
            - 'magnitude' determines the extent of the modification (-2: Hardly decrease, -1: Decrease, 1: Increase, 2: Hardly increased)
            - After the modification the target's stats are recalculated
        """

        if stat == "attack":
            target.attackbuff += magnitude
        elif stat == "defense":
            target.defensebuff += magnitude
        elif stat == "speattack":
            target.speattackbuff += magnitude
        elif stat == "spedefense":
            target.spedefensebuff += magnitude
        elif stat == "speed":
            target.speedbuff += magnitude
        target.recalculate_stats()
        
        print(f"{target.name}'s {stat} was modified by {magnitude}")
        
        if stat == "attack":
            print(f"{target.name}'s {stat} is now {target.attack}")
        elif stat == "defense":
            print(f"{target.name}'s {stat} is now {target.defense}")
        elif stat == "speattack":
            print(f"{target.name}'s {stat} is now {target.speattack}")
        elif stat == "spedefense":
            print(f"{target.name}'s {stat} is now {target.spedefense}")
        elif stat == "speed":
            print(f"{target.name}'s {stat} is now {target.speed}")
                
                
                        
    
    def executeStatusEffect(self, target, effectAccuracy: float, effectType: PokemonType):
        
        """
        When a movement is used, calculates if the status effect connected and if so applies the effect to the target
        
        Args:
            self(Movement): The Movement instance
            target(Pokemon): The Pokemon that will get the status
            effectAccuracy(float): The probability that the status will be applied (1-100)
            effectType(PokemonType): The type of status that the movement will cause to the target
            
        Returns:
            None
        
        Comments:
            - Ensures the target is a Pokemon instance
            - Checks wether the target already has a status (in this case a new status can not be applied)
            - If the status change connected and the pokemon did not have a status it applies the new status 
            - Prints a statement to inform the user of the status change
        """
        

        if target.has_status()==False:
            if self.connected(effectAccuracy):
                target.status = effectType
                print(f"{target.name} is {c.POKEMON_STATUS[effectType]}.")