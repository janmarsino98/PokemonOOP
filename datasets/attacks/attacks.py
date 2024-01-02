from datasets.movement import Movement
from datasets.pokemontype import PokemonType

#Target can be enemy, own or choose

quickattack = Movement("Quickattack", 30, 30, 100, PokemonType.NORMAL, None,target="enemy")


thund_wave = Movement(
        name="Thunder Wave",
        power = 0,
        pp = 20,
        accuracy=90,
        typ=PokemonType.ELECTRIC,
        effects=[
            {"category": "status", "type": "paralyze", "probability": 90, "target": None},
            {"category": "statChange", "stat": "attack", "magnitude": -1, "probability":20, "target":None}
        ],
        target="enemy"
)