from random import random
from datasets.pokemontype import PokemonType
import datasets.constants as c
from .targetype import *
from .pokemon import Pokemon

class Movement:
    def __init__(self, name: str, power: int, pp: int, accuracy: float, typ: PokemonType, effects: list, default_target):
        self.name = name
        self.power = power
        self.pp = pp
        self.accuracy = accuracy
        self.typ = typ
        self.effects = effects
        self.target = None
        self.default_target = default_target
    
    def movement_connected(self) -> bool:
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
        
    def deal_dmg(self, user: Pokemon, target: Pokemon):
        
        """
        Calculates and applies damage from the curret movement to the target
        
        Args:
            self(Movement): The Movement instance
            user(Pokemon): The user Pokemon that performs the movement
            target(Pokemon): The target Pokemon that receives the damage
            
        Returns:
            None
            
        Notes:
            - Each movement will role to get less or more damage
            - 

            
        """
        
        if self.movement_connected(self):
            if self.power != 0:
                dmg = int(((((2 * user.level * self.critical()) / 5 + 2) * self.power + 2) * user.attack / target.defense / 50) * self.movement_stab(self) * user.extra_dmg_type(self, target) \
                * random.randint(217, 255) / 255)
                print(f"The damage taken was {dmg}")
                target.set_health(dmg)
                
            else:
                pass
            
            self.execute_effects(user=self, defender=target, chosen_target = chosen_target)
            if not target.is_alive():
                print(f"{target.name} is defeated")
                
            else:
                print(f"{target.name} remaining HP is {target.health}")
            
            
        else:
            print(f"{self.name} did not connect")

    def movement_stab(self, user: Pokemon) -> float:
    
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

    
    def critical(self) -> int:
    
        """
        Calculates wether a movement scored a critical move or not
        
        Args:
            self(Movement): The Movement instance
            
        Returns:
            1 if no criticial
            2 if critical
            
        Notes:
            - Returns one of theese numbers to use them  in the deal_dmg() formula
    
        """

        threshold = self.speed / 512
        current = random.random()
        if current < threshold:
            print("It was a critical move")
            return 2
            
        else:
            return 1
        
    def execute_effects(self, user, defender, chosen_target = None ):
        
        # This function will execute the different effects of a movement
        
        
        
        if self.effects is None:
            
            # If the movement has no effects it will do nothing.
            
            pass
        
        else:
            
            for effect in self.effects:
                
                #for each effect we will determine which is the target of that effect according to the target of that effect. The TargetType can be OWN, ENEMY or CHOOSE
                
                #PRIORITY MOVEMENTS
                
                if effect["category"] == EffectCategory.PRIORITY:
                    print("The movement will hit first")
                
                
                else:
                    target = None
                    
                    if effect["target"] == TargetType.OWN:
                        
                        #If the TargetType is OWN the user will receive the effect
                        
                        target = user
                    
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
                        self.executeHealEffect(user=user, amount_to_heal=user.dmg/2)
                        
    
    def executeHealEffect(self, user, amount_to_heal):
        user.set_health(amount_to_heal)
        if amount_to_heal != 0:
            print(f"{user.name} healed {amount_to_heal} hp's.")

                
    def executeStatChange(self, stat: str, target: Pokemon, magnitude: float):
        
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
        
        if isinstance(target, Pokemon):
            if target.has_status()==False:
                if self.connected(effectAccuracy):
                    target.status = effectType
                    print(f"{target.name} is {c.POKEMON_STATUS[effectType]}.")
                    
        else:
            print(f"The target {target} is not a Pokemon")
                    

    def connected(self, accuracy: float) -> bool:
        return random() < accuracy/100