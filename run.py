from datasets.movement import Movement
from datasets.constants import TABLETYPES
from datasets.pokemon import Pokemon
from datasets.pokemontype import PokemonType
from datasets.trainer import Trainer
from datasets.battle import Battle
from datasets.attacks import attacks
from datasets.targetype import *



Pikachu = Pokemon("Pikachu", 50, 100, 55, 30, 90, 50, 50, PokemonType.ELECTRIC, None, [attacks.quickattack, attacks.thund_wave, attacks.flamethrower, None])
Raichu = Pokemon("Raichu", 50, 100, 100, 30, 90, 100, 100, PokemonType.ELECTRIC, None, [attacks.quickattack, None, None, None])

jan = Trainer("Jan")
enemic = Trainer("Enemy")

new_battle = Battle(jan, enemic)
jan.set_pokemon(0, Pikachu)
enemic. set_pokemon(0, Raichu)

for i in range(20):
    new_battle.battle_loop()
    
quickattack = Movement("Quickattack", 30, 30, 100, PokemonType.NORMAL, effects=[{"category": EffectCategory.PRIORITY}], default_target=TargetType.ENEMY)
