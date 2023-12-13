from datasets.movement import Movement
from datasets.constants import TABLETYPES
from datasets.pokemon import Pokemon
from datasets.pokemontype import PokemonType

quickattack = Movement("Quickattack", 30, 30, 100, PokemonType.NORMAL, "P")
Pikachu = Pokemon("Pikachu", 50, 100, 50,100, 100, 100, 100, PokemonType.ELECTRIC, None, [quickattack, "", "", ""])
Raichu = Pokemon("Raichu", 50, 100, 100, 30, 100, 100, 100, PokemonType.ELECTRIC, None, [quickattack, "", "", ""])

