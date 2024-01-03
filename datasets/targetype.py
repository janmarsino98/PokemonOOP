from enum import Enum

class TargetType(Enum):
    OWN = 1
    ENEMY = 2
    CHOOSE = 3
    
class EffectCategory(Enum):
    PRIORITY = 1
    STATCHANGE = 2
    STATUSEFFECT = 3
    
class EffectType(Enum):
    PARALYZE = 1
    POISON = 2
    BURN = 3
    ICE = 4
    SLEEP = 5