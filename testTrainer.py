from datasets.trainer import Trainer
from datasets.pokemons.pokemons import *
from datasets.battle import Battle

# CREATE AN INSTANCE OF A TRAINER
jan = Trainer("Jan")
roger = Trainer("Roger")

# CREATE A BATTLE INSTANCE BETWEEN 2 POKEMONS
battle = Battle(jan, roger)
jan.set_pokemon(0, Pikachu)
roger.set_pokemon(0,Raichu)

battle.run_first_turn()
for _ in range(5):
    battle.run_turn()