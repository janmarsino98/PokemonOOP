from datasets.movement import Movement
from pokemontype import PokemonType

quickattack = Movement("quickattack", 40, 35, 100, "Normal","P")

thund_wave = Movement(
    name="Thunder Wave",
    power=0,
    pp=10,
    accuracy=80,
    typ=PokemonType.ELECTRIC,
    effects={
        "category": "status",
        "type": "paralyze",
        "probability": 90
        },
    target=Raichu
)
