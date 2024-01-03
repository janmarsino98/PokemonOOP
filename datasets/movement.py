from random import random
from datasets.pokemontype import PokemonType
import datasets.constants as c
from .targetype import *

class Movement:
    def __init__(self, name: str, power: int, pp: int, accuracy: float, typ: PokemonType, effects, default_target):
        self.name = name
        self.power = power
        self.pp = pp
        self.accuracy = accuracy
        self.typ = typ
        self.effects = effects
        self.target = None
        self.default_target = default_target
        
    def execute_effects(self, user, defender, chosen_target = None ):
        from .pokemon import Pokemon
        
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
                
    def executeStatChange(self, stat: str, target, magnitude: float):

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
                        
    
    def executeStatusEffect(self, target, effectAccuracy: float, effectType: PokemonType):
        from .pokemon import Pokemon
        if isinstance(target, Pokemon):
            if target.has_status():
                print(f"{target.name} is already in {target.status} status so your movement can't {effectType} it")
                
            else:
                if self.connected(effectAccuracy):
                    target.status = effectType
                    print(f"{target.name} is now in {effectType} state.")
                    
        else:
            print(f"The target {target} is not a Pokemon")
                    

    def connected(self, accuracy: float) -> bool:
        return random() < accuracy/100