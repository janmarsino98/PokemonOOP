from enum import Enum
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datasets.pokemon import Pokemon
    from datasets.movement import Movement
    
    
class TargetType(Enum):
    OWN = 1
    ENEMY = 2
    CHOOSE = 3