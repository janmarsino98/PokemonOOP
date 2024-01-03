from datasets.movement import Movement
from datasets.pokemontype import PokemonType
from datasets.targetype import TargetType, EffectCategory, EffectType

#Target can be enemy, own or choose


#Quick attack 
quickattack = Movement("Quickattack", 30, 30, 100, PokemonType.NORMAL, effects=[{"category": EffectCategory.PRIORITY}], default_target=TargetType.ENEMY)


thund_wave = Movement(
        name="Thunder Wave",
        power = 0,
        pp = 20,
        accuracy=90,
        typ=PokemonType.ELECTRIC,
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": EffectType.PARALYZE, "probability": 90, "target": None},
            {"category": EffectCategory.STATCHANGE, "stat": "attack", "magnitude": -1, "probability":20, "target":None}
        ],
        default_target=TargetType.ENEMY
)

