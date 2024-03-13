from ..movement import Movement
from ..attacks import attacks
from ..pokemontype import PokemonType
from ..pokemon import Pokemon




Pikachu = Pokemon("Pikachu", 50, 100, 55, 30, 90, 50, 50, PokemonType.ELECTRIC, None, [attacks.quickattack, attacks.thund_wave, attacks.flamethrower, attacks.bonemerang])
Raichu = Pokemon("Raichu", 50, 100, 100, 30, 90, 100, 100, PokemonType.ELECTRIC, None, [attacks.quickattack, None, None, None])