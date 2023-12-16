from datasets.movement import Movement
from datasets.constants import TABLETYPES
from datasets.pokemon import Pokemon
from datasets.pokemontype import PokemonType

quickattack = Movement("Quickattack", 30, 30, 100, PokemonType.NORMAL, "P", "x")
Pikachu = Pokemon("Pikachu", 50, 100, 50,100, 100, 100, 100, PokemonType.ELECTRIC, None, [quickattack, "", "", ""])
Raichu = Pokemon("Raichu", 50, 100, 100, 30, 100, 100, 100, PokemonType.ELECTRIC, None, [quickattack, "", "", ""])


thund_wave = Movement(
        name="Thunder Wave",
        power = 0,
        pp = 20,
        accuracy=90,
        typ=PokemonType.ELECTRIC,
        effects=[
            {"category": "status", "type": "paralyze", "probability": 90},
            {"category": "statChange", "stat": "attack", "magnitude": -1, "probability":20, "target":Raichu}
        ],
        target=Raichu
)

print(Raichu.attack)
Pikachu.attack_enemy(thund_wave, Raichu)
print(Raichu.attack)
Pikachu.attack_enemy(thund_wave, Raichu)
print(Raichu.attack)
Pikachu.attack_enemy(thund_wave, Raichu)
print(Raichu.attack)