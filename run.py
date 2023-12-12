from datasets import *


quickattack = movement("Quick attack", 130, 40, 100, "normal", "p")
noattack = movement("-", 0, 0, 0, "X", "X")
        
Pikachu = Pokemon("Pikachu", 50, 100, 50, 100, 100, 100, 100, Type.ELECTRIC, [quickattack, noattack, noattack, noattack])
Raichu = Pokemon("Raichu", 50, 100, 100, 30, 100, 100, 100, Type.ELECTRIC, [quickattack, noattack, noattack, noattack])