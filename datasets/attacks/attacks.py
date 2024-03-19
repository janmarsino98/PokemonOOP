from datasets.movement import Movement
from datasets.pokemontype import PokemonType
from datasets.targetype import TargetType
from datasets.effectCategory import EffectCategory
from datasets.statusType import StatusType
from datasets.effect import *
import datasets.constants as c
import json

#Target can be enemy, own or choose


# No definitiu
quickattack = Movement("Quickattack", 30, 30, 100, PokemonType.NORMAL, effects=[{"category": EffectCategory.PRIORITY}], targetType=TargetType.ENEMY)

# No definitiu
thund_wave = Movement(
        name="Thunder Wave",
        power = 0,
        pp = 20,
        accuracy=90,
        typ=PokemonType.ELECTRIC,
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": StatusType.PARALYZE, "probability": 90, "target": TargetType.ENEMY},
            {"category": EffectCategory.STATCHANGE, "stat": "attack", "magnitude": 1, "probability":20, "target":TargetType.OWN}
        ],
        targetType=TargetType.ENEMY
)

halfheal = Movement(
        name = "halfheal",
        power = 0,
        pp = 1,
        accuracy= 100,
        typ = None,
        effects = [
                {"category": EffectCategory.HEAL, "heal_amount": 30, "probability":100, "target":TargetType.OWN}
        ],targetType=TargetType.OWN
)


#Ok
acid = Movement(
        name="Acid",
        power = c.MOVEMENTS_D["Acid"]["power"],
        pp = c.MOVEMENTS_D["Acid"]["pp"],
        accuracy=c.MOVEMENTS_D["Acid"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Acid"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "defense", "magnitude": 1, "probability":100, "target":TargetType.ENEMY},
            {"category": EffectCategory.HEAL, "heal_amount": 30, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.ENEMY
)

dict_file = r"movementsdict.txt"
with open(dict_file, "r") as file:
    move_d = json.load(file)

#Ok
acid_armor = Movement(
        name="Acid Armor",
        power = c.MOVEMENTS_D["Acid Armor"]["power"],
        pp = c.MOVEMENTS_D["Acid Armor"]["pp"],
        accuracy=c.MOVEMENTS_D["Acid Armor"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Acid Armor"]["type"].upper()],
        effects=[ 
            {"category": EffectCategory.STATCHANGE, "stat": "defense", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#OK
agility = Movement(
        name="Agility",
        power = c.MOVEMENTS_D["Agility"]["power"],
        pp = c.MOVEMENTS_D["Agility"]["pp"],
        accuracy=c.MOVEMENTS_D["Agility"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Agility"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#Ok
amnesia = Movement(
        name="Amnesia",
        power = c.MOVEMENTS_D["Amnesia"]["power"],
        pp = c.MOVEMENTS_D["Amnesia"]["pp"],
        accuracy=c.MOVEMENTS_D["Amnesia"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Amnesia"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "spedefense", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#Ok
aurora_beam = Movement(
        name="Aurora Beam",
        power = c.MOVEMENTS_D["Aurora Beam"]["power"],
        pp = c.MOVEMENTS_D["Aurora Beam"]["pp"],
        accuracy=c.MOVEMENTS_D["Aurora Beam"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Aurora Beam"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "defense", "magnitude": -1, "probability":10, "target":TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)

#OK
barrage = Movement(
        name="Barrage",
        power = c.MOVEMENTS_D["Barrage"]["power"],
        pp = c.MOVEMENTS_D["Barrage"]["pp"],
        accuracy=c.MOVEMENTS_D["Barrage"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Barrage"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#OK
barrier = Movement(
        name="Barrier",
        power = c.MOVEMENTS_D["Barrier"]["power"],
        pp = c.MOVEMENTS_D["Barrier"]["pp"],
        accuracy=c.MOVEMENTS_D["Barrier"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Barrier"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "defense", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

bide = Movement(
        name="Bide",
        power = c.MOVEMENTS_D["Bide"]["power"],
        pp = c.MOVEMENTS_D["Bide"]["pp"],
        accuracy=c.MOVEMENTS_D["Bide"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Bide"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

bind = Movement(
        name="Bind",
        power = c.MOVEMENTS_D["Bind"]["power"],
        pp = c.MOVEMENTS_D["Bind"]["pp"],
        accuracy=c.MOVEMENTS_D["Bind"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Bind"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#Ok
blizzard = Movement(
        name="Blizzard",
        power = c.MOVEMENTS_D["Blizzard"]["power"],
        pp = c.MOVEMENTS_D["Blizzard"]["pp"],
        accuracy=c.MOVEMENTS_D["Blizzard"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Blizzard"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": StatusType.ICE, "probability": 10, "target": TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)

#Ok
body_slam = Movement(
        name="Body Slam",
        power = c.MOVEMENTS_D["Body Slam"]["power"],
        pp = c.MOVEMENTS_D["Body Slam"]["pp"],
        accuracy=c.MOVEMENTS_D["Body Slam"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Body Slam"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": StatusType.PARALYZE, "probability": 30, "target": TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)

bone_club = Movement(
        name="Bone Club",
        power = c.MOVEMENTS_D["Bone Club"]["power"],
        pp = c.MOVEMENTS_D["Bone Club"]["pp"],
        accuracy=c.MOVEMENTS_D["Bone Club"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Bone Club"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

bonemerang = Movement(
        name="Bonemerang",
        power = c.MOVEMENTS_D["Bonemerang"]["power"],
        pp = c.MOVEMENTS_D["Bonemerang"]["pp"],
        accuracy=c.MOVEMENTS_D["Bonemerang"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Bonemerang"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN},
        ],
        targetType=TargetType.OWN
)

#Ok
bubble = Movement(
        name="Bubble",
        power = c.MOVEMENTS_D["Bubble"]["power"],
        pp = c.MOVEMENTS_D["Bubble"]["pp"],
        accuracy=c.MOVEMENTS_D["Bubble"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Bubble"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 1, "probability":10, "target":TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)

#Ok
bubble_beam = Movement(
        name="Bubble Beam",
        power = c.MOVEMENTS_D["Bubble Beam"]["power"],
        pp = c.MOVEMENTS_D["Bubble Beam"]["pp"],
        accuracy=c.MOVEMENTS_D["Bubble Beam"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Bubble Beam"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 1, "probability":10, "target":TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)

clamp = Movement(
        name="Clamp",
        power = c.MOVEMENTS_D["Clamp"]["power"],
        pp = c.MOVEMENTS_D["Clamp"]["pp"],
        accuracy=c.MOVEMENTS_D["Clamp"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Clamp"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

comet_punch = Movement(
        name="Comet Punch",
        power = c.MOVEMENTS_D["Comet Punch"]["power"],
        pp = c.MOVEMENTS_D["Comet Punch"]["pp"],
        accuracy=c.MOVEMENTS_D["Comet Punch"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Comet Punch"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

confuse_ray = Movement(
        name="Confuse Ray",
        power = c.MOVEMENTS_D["Confuse Ray"]["power"],
        pp = c.MOVEMENTS_D["Confuse Ray"]["pp"],
        accuracy=c.MOVEMENTS_D["Confuse Ray"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Confuse Ray"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

confusion = Movement(
        name="Confusion",
        power = c.MOVEMENTS_D["Confusion"]["power"],
        pp = c.MOVEMENTS_D["Confusion"]["pp"],
        accuracy=c.MOVEMENTS_D["Confusion"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Confusion"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

constrict = Movement(
        name="Constrict",
        power = c.MOVEMENTS_D["Constrict"]["power"],
        pp = c.MOVEMENTS_D["Constrict"]["pp"],
        accuracy=c.MOVEMENTS_D["Constrict"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Constrict"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 1, "probability":10, "target":TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)

conversion = Movement(
        name="Conversion",
        power = c.MOVEMENTS_D["Conversion"]["power"],
        pp = c.MOVEMENTS_D["Conversion"]["pp"],
        accuracy=c.MOVEMENTS_D["Conversion"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Conversion"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

counter = Movement(
        name="Counter",
        power = c.MOVEMENTS_D["Counter"]["power"],
        pp = c.MOVEMENTS_D["Counter"]["pp"],
        accuracy=c.MOVEMENTS_D["Counter"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Counter"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

crabhammer = Movement(
        name="Crabhammer",
        power = c.MOVEMENTS_D["Crabhammer"]["power"],
        pp = c.MOVEMENTS_D["Crabhammer"]["pp"],
        accuracy=c.MOVEMENTS_D["Crabhammer"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Crabhammer"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

cut = Movement(
        name="Cut",
        power = c.MOVEMENTS_D["Cut"]["power"],
        pp = c.MOVEMENTS_D["Cut"]["pp"],
        accuracy=c.MOVEMENTS_D["Cut"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Cut"]["type"].upper()],
        effects=[
        ],
        targetType=TargetType.ENEMY
)

defense_curl = Movement(
        name="Defense Curl",
        power = c.MOVEMENTS_D["Defense Curl"]["power"],
        pp = c.MOVEMENTS_D["Defense Curl"]["pp"],
        accuracy=c.MOVEMENTS_D["Defense Curl"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Defense Curl"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "defense", "magnitude": 1, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

dig = Movement(
        name="Dig",
        power = c.MOVEMENTS_D["Dig"]["power"],
        pp = c.MOVEMENTS_D["Dig"]["pp"],
        accuracy=c.MOVEMENTS_D["Dig"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Dig"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

disable = Movement(
        name="Disable",
        power = c.MOVEMENTS_D["Disable"]["power"],
        pp = c.MOVEMENTS_D["Disable"]["pp"],
        accuracy=c.MOVEMENTS_D["Disable"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Disable"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

dizzy_punch = Movement(
        name="Dizzy Punch",
        power = c.MOVEMENTS_D["Dizzy Punch"]["power"],
        pp = c.MOVEMENTS_D["Dizzy Punch"]["pp"],
        accuracy=c.MOVEMENTS_D["Dizzy Punch"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Dizzy Punch"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

double_kick = Movement(
        name="Double Kick",
        power = c.MOVEMENTS_D["Double Kick"]["power"],
        pp = c.MOVEMENTS_D["Double Kick"]["pp"],
        accuracy=c.MOVEMENTS_D["Double Kick"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Double Kick"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)


double_slap = Movement(
        name="Double Slap",
        power = c.MOVEMENTS_D["Double Slap"]["power"],
        pp = c.MOVEMENTS_D["Double Slap"]["pp"],
        accuracy=c.MOVEMENTS_D["Double Slap"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Double Slap"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

double_team = Movement(
        name="Double Team",
        power = c.MOVEMENTS_D["Double Team"]["power"],
        pp = c.MOVEMENTS_D["Double Team"]["pp"],
        accuracy=c.MOVEMENTS_D["Double Team"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Double Team"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

double_edge = Movement(
        name="Double-Edge",
        power = c.MOVEMENTS_D["Double-Edge"]["power"],
        pp = c.MOVEMENTS_D["Double-Edge"]["pp"],
        accuracy=c.MOVEMENTS_D["Double-Edge"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Double-Edge"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)


dragon_rage = Movement(
        name="Dragon Rage",
        power = c.MOVEMENTS_D["Dragon Rage"]["power"],
        pp = c.MOVEMENTS_D["Dragon Rage"]["pp"],
        accuracy=c.MOVEMENTS_D["Dragon Rage"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Dragon Rage"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)


dream_eater = Movement(
        name="Dream Eater",
        power = c.MOVEMENTS_D["Dream Eater"]["power"],
        pp = c.MOVEMENTS_D["Dream Eater"]["pp"],
        accuracy=c.MOVEMENTS_D["Dream Eater"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Dream Eater"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#Ok
drill_peck = Movement(
        name="Drill Peck",
        power = c.MOVEMENTS_D["Drill Peck"]["power"],
        pp = c.MOVEMENTS_D["Drill Peck"]["pp"],
        accuracy=c.MOVEMENTS_D["Drill Peck"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Drill Peck"]["type"].upper()],
        effects=[
        ],
        targetType=TargetType.ENEMY
)


earthquake = Movement(
        name="Earthquake",
        power = c.MOVEMENTS_D["Earthquake"]["power"],
        pp = c.MOVEMENTS_D["Earthquake"]["pp"],
        accuracy=c.MOVEMENTS_D["Earthquake"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Earthquake"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#Ok
egg_bomb = Movement(
        name="Egg Bomb",
        power = c.MOVEMENTS_D["Egg Bomb"]["power"],
        pp = c.MOVEMENTS_D["Egg Bomb"]["pp"],
        accuracy=c.MOVEMENTS_D["Egg Bomb"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Egg Bomb"]["type"].upper()],
        effects=[
        ],
        targetType=TargetType.ENEMY
)

#Ok
ember = Movement(
        name="Ember",
        power = c.MOVEMENTS_D["Ember"]["power"],
        pp = c.MOVEMENTS_D["Ember"]["pp"],
        accuracy=c.MOVEMENTS_D["Ember"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Ember"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": StatusType.BURN, "probability": 10, "target": TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)


explosion = Movement(
        name="Explosion",
        power = c.MOVEMENTS_D["Explosion"]["power"],
        pp = c.MOVEMENTS_D["Explosion"]["pp"],
        accuracy=c.MOVEMENTS_D["Explosion"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Explosion"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#Ok
fire_blast = Movement(
        name="Fire Blast",
        power = c.MOVEMENTS_D["Fire Blast"]["power"],
        pp = c.MOVEMENTS_D["Fire Blast"]["pp"],
        accuracy=c.MOVEMENTS_D["Fire Blast"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Fire Blast"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": StatusType.BURN, "probability": 10, "target": TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)

#Ok
fire_punch = Movement(
        name="Fire Punch",
        power = c.MOVEMENTS_D["Fire Punch"]["power"],
        pp = c.MOVEMENTS_D["Fire Punch"]["pp"],
        accuracy=c.MOVEMENTS_D["Fire Punch"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Fire Punch"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": StatusType.BURN, "probability": 10, "target": TargetType.ENEMY}
        ],
        targetType=TargetType.ENEMY
)


fire_spin = Movement(
        name="Fire Spin",
        power = c.MOVEMENTS_D["Fire Spin"]["power"],
        pp = c.MOVEMENTS_D["Fire Spin"]["pp"],
        accuracy=c.MOVEMENTS_D["Fire Spin"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Fire Spin"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)


fissure = Movement(
        name="Fissure",
        power = c.MOVEMENTS_D["Fissure"]["power"],
        pp = c.MOVEMENTS_D["Fissure"]["pp"],
        accuracy=c.MOVEMENTS_D["Fissure"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Fissure"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATCHANGE, "stat": "speed", "magnitude": 2, "probability":100, "target":TargetType.OWN}
        ],
        targetType=TargetType.OWN
)

#Ok
flamethrower = Movement(
        name="Flamethrower",
        power = c.MOVEMENTS_D["Flamethrower"]["power"],
        pp = c.MOVEMENTS_D["Flamethrower"]["pp"],
        accuracy=c.MOVEMENTS_D["Flamethrower"]["accuracy"],
        typ=PokemonType[c.MOVEMENTS_D["Flamethrower"]["type"].upper()],
        effects=[
            {"category": EffectCategory.STATUSEFFECT, "type": StatusType.BURN, "probability": 10, "target": TargetType.ENEMY}
        ],
        targetType=TargetType.OWN
)