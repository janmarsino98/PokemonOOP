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
        
        for effect in self.effects:
            
            #PRIORITY MOVEMENTS
            
            if effect["category"] == "priority":
                print("The movement will hit first")
                
            
            #STAT BUFF/NERF MOVEMENTS    
            
            elif effect["category"] == "statChange":
                if effect["stat"] == "attack":
                    effect["target"].attackbuff += effect["magnitude"]
                elif effect["stat"] == "deffense":
                    effect["target"].defensebuff += effect["magnitude"]
                elif effect["stat"] == "speattack":
                    effect["target"].speattackbuff += effect["magnitude"]
                elif effect["stat"] == "spedefense":
                    effect["target"].spedefense += effect["magnitude"]
                elif effect["stat"] == "speed":
                    effect["target"].speedbuff += effect["magnitude"]
                effect["target"].recalculate_stats()
                print(f"{effect['target'].name} {effect['stat']} was modified by {effect['magnitude']}")
                
                
            #STATUS MOVEMENTS
                
            elif effect["category"] == "status":
                if self.target.has_status():
                    print(f"{self.target.name} is already in {self.target.status} status so your movement can't {effect['type']} it")
                
                else:
                    if self.connected(effect["probability"]):
                        self.target.status = effect['type']
                        print(f"{self.target.name} is now in {effect['type']} state.")
                

    def connected(self, accuracy):
        return random() < accuracy/100