from datasets.pokemon import Pokemon
from datasets.pokemons.pokemons import *
from datasets.movement import Movement
from datasets.targetype import TargetType

pikachu = Pikachu

pikachu.status = "Paralized"
print(pikachu.has_status())

print(pikachu.is_alive())

pikachu.select_movement()


quick_attack = Movement("Quickattack", 30, 30, 100, PokemonType.NORMAL, None, TargetType.ENEMY)
