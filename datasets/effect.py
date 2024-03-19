from datasets.effectCategory import EffectCategory
from typing import TYPE_CHECKING
import random
from datasets.targetype import TargetType
from datasets.statusType import StatusType

if TYPE_CHECKING:
    from datasets.pokemon import Pokemon
    from datasets.movement import Movement
    from datasets.targetype import TargetType
    from datasets.statusType import StatusType
    

class Effect:
    def __init__(self, user: "Pokemon", enemy: "Pokemon", category: EffectCategory, probability: float):
        self.user = user
        self.enemy = enemy
        self.category = category
        self.probability = probability
        
    def connected(self) -> bool:
        """
        Decides if a effect connected or failed
        
        Args:
            self(Effect): The Effect instance
            
        Returns:
            bool
            True if connected
            False if failed

        """    

        threshold = random.random()
        return threshold < self.probability / 100
        
class StatChangeEffect(Effect):
    
    def __init__(self, user, enemy, stat, magnitude, probability: float, targetType: "TargetType"):
        super().__init__(user, enemy, EffectCategory.STATCHANGE, probability)
        self.stat = stat
        self.magnitude = magnitude
        self.targetType = targetType
        
        self.target: "Pokemon"
        if self.targetType == TargetType.ENEMY:
            self.target = enemy
        else:
            self.target = self.user
            
    def apply(self):
        if self.connected():
            self.target.modify_stat(self.stat, self.magnitude)
            if self.magnitude < 0:
                print(f"{self.target.name}'s {self.stat} was reduced.")
                
            else:
                print(f"{self.target.name}'s {self.stat} was increased.")
                
class HealEffect(Effect):
    
    def __init__(self, user, enemy, heal_amount: float, probability: float, targetType: "TargetType"):
        super().__init__(user, enemy, EffectCategory.HEAL, probability)
        self.heal_amount = heal_amount
        self.targetType = targetType
        self.target: "Pokemon"
        if self.targetType == TargetType.ENEMY:
            self.target = enemy
        else:
            self.target = self.user
            
    def apply(self):
        if self.connected():
            self.target.heal(self.heal_amount)
            print(f"{self.target.name} was healed and is now at {self.target.health * 100 / self.target.max_health}% health.")
        
class StatusEffect(Effect):
    def __init__(self, user, enemy, type: "StatusType", probability: float, targetType: "TargetType"):
        super().__init__(user, enemy, EffectCategory.STATUSEFFECT, probability)
        self.type = type
        self.targetType = targetType
        self.target: "Pokemon"
        if self.targetType == TargetType.ENEMY:
            self.target = enemy
        else:
            self.target = self.user
        
    def apply(self):
        if self.connected() & self.target.has_status()==False:
            self.target.status = self.type
            if self.type == StatusType.PARALYZE:
                print(f"{self.target.name} is now paralyzed.")
                
            elif self.type == StatusType.BURN:
                print(f"{self.target.name} is now burnt.")
            elif self.type == StatusType.ICE:
                print(f"{self.target.name} is now freezed.")
            elif self.type == StatusType.POISON:
                print(f"{self.target.name} is now poisoned.")
            elif self.type == StatusType.SLEEP:
                print(f"{self.target.name} is now sleeping.")