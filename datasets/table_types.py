from Pokemontype import PokemonType

table_types = {PokemonType.NORMAL:
                [[],
                [PokemonType.ROCK], 
                [PokemonType.GHOST]],
               PokemonType.FIRE:
                   [[PokemonType.GRASS, PokemonType.ICE, PokemonType.BUG],
                    [PokemonType.FIRE, PokemonType.WATER, PokemonType.ROCK, PokemonType.DRAGON], 
                    []],
               PokemonType.WATER:
                   [[PokemonType.FIRE, PokemonType.GROUND, PokemonType.ROCK],
                    [PokemonType.WATER, PokemonType.GRASS, PokemonType.DRAGON],
                    []],
               PokemonType.ELECTRIC:
                   [[PokemonType.WATER, PokemonType.FLYING],
                    [PokemonType.ELECTRIC, PokemonType.GRASS],
                    [PokemonType.GROUND]],
               PokemonType.GRASS:
                   [[PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK],
                    [PokemonType.FIRE, PokemonType.GRASS, PokemonType.POISON, PokemonType.FLYING, PokemonType.BUG, PokemonType.DRAGON],
                    []]
               }
        