from datasets.Pokemon import Pokemon
from datasets.movement import movement
from datasets.Pokemontype import PokemonType
from datasets import *


quickattack = movement("quickattack", 20, 20, 100, PokemonType.NORMAL, "P")
noattack = movement("-", 0, 0, 0, "X", "X")
        
Pikachu = Pokemon("Pikachu", 50, 100, 50, 100, 100, 100, 100, PokemonType.ELECTRIC, None, [quickattack, noattack, noattack, noattack])
Raichu = Pokemon("Raichu", 50, 100, 100, 30, 100, 100, 100, PokemonType.ELECTRIC, None, [quickattack, noattack, noattack, noattack])

Pikachu.attack_enemy(quickattack, Raichu)