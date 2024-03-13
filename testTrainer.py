from datasets.trainer import Trainer
from datasets.pokemons.pokemons import *
from datasets.battle import Battle

jan = Trainer("Jan")
roger = Trainer("Roger")
battle = Battle(jan, roger)
jan_pikachu = Pikachu
roger_raichu = Raichu

jan.set_pokemon(0, jan_pikachu)
roger.set_pokemon(0,roger_raichu)

jan.set_battlefield_pokemon(jan_pikachu)
roger.set_battlefield_pokemon(roger_raichu)

jan_pikachu.set_health(40)
jan_pikachu.use_movement(jan_pikachu.movements[3],roger_raichu)