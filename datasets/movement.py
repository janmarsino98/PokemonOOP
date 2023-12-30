from random import random
from datasets.pokemontype import PokemonType
import datasets.constants as c

class Movement:
    def __init__(self, name, power, pp, accuracy, typ, effects, target):
        self.name = name
        self.power = power
        self.pp = pp
        self.accuracy = accuracy
        self.typ = typ
        self.effects = effects
        self.target = target
        
    def execute_effects(self):
        if self.effects == None:
            pass
        else:
            for effect in self.effects:
                
                #PRIORITY MOVEMENTS
                
                if effect["category"] == "priority":
                    print("The movement will hit first")
                    
                
                #STAT BUFF/NERF MOVEMENTS    
                
                elif effect["category"] == "statChange":
                    self.executeStatChange(stat=effect["stat"], target=effect["target"], magnitude=effect["magnitude"])
                    
                    
                #STATUS MOVEMENTS
                    
                elif effect["category"] == "status":
                    self.executeStatusEffect(target=effect["target"], effectAccuracy=effect["probability"], effectType=effect["type"])
                
    def executeStatChange(self, stat, target, magnitude):
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
                        
    
    def executeStatusEffect(self, target, effectAccuracy, effectType):
        if target.has_status():
            print(f"{target.name} is already in {target.status} status so your movement can't {effectType} it")
            
        else:
            if self.connected(effectAccuracy):
                target.status = effectType
                print(f"{target.name} is now in {effectType} state.")
                    

    def connected(self, accuracy):
        return random() < accuracy/100