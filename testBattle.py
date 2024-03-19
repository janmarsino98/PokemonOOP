from datasets.trainer import Trainer
from datasets.battle import Battle
from datasets.pokemons.pokemons import *

jan = Trainer("Jan")
roger = Trainer("Roger")
jan.set_pokemon(0, Pikachu)
roger.set_pokemon(0, Raichu)

main_battle = Battle(jan, roger)

main_battle.run_first_turn()
main_battle.run_turn()