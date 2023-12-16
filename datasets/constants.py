from datasets.pokemontype import PokemonType

# FOR EACH TYPE WE HAVE: VERY EFFECTIVE, NOT VERY EFFECTIVE, IMMUNE

TABLETYPES = {
    PokemonType.NORMAL: [
        [],
        [PokemonType.ROCK],
        [PokemonType.GHOST],
    ],
    PokemonType.FIRE: [
        [PokemonType.GRASS, PokemonType.ICE, PokemonType.BUG],
        [PokemonType.FIRE, PokemonType.WATER, PokemonType.ROCK, PokemonType.DRAGON],
        [],
    ],
    PokemonType.WATER: [
        [PokemonType.FIRE, PokemonType.GROUND, PokemonType.ROCK],
        [PokemonType.WATER, PokemonType.GRASS, PokemonType.DRAGON],
        [],
    ],
    PokemonType.ELECTRIC: [
        [PokemonType.WATER, PokemonType.FLYING],
        [PokemonType.ELECTRIC, PokemonType.GRASS],
        [PokemonType.GROUND],
    ],
    PokemonType.GRASS: [
        [PokemonType.WATER, PokemonType.GROUND, PokemonType.ROCK],
        [
            PokemonType.FIRE,
            PokemonType.GRASS,
            PokemonType.POISON,
            PokemonType.FLYING,
            PokemonType.BUG,
            PokemonType.DRAGON,
        ],
        [],
    ],
    PokemonType.ROCK: [
        [PokemonType.FIRE, PokemonType.ICE, PokemonType.FLYING, PokemonType.BUG],
        [PokemonType.WATER, PokemonType.GRASS, PokemonType.FIGHTING, PokemonType.GROUND],
        [],
    ],
    PokemonType.GHOST: [
        [PokemonType.NORMAL, PokemonType.FIGHTING],
        [PokemonType.POISON, PokemonType.BUG],
        [PokemonType.GHOST],
    ],
    PokemonType.ICE: [
        [PokemonType.GRASS, PokemonType.GROUND, PokemonType.FLYING, PokemonType.DRAGON],
        [PokemonType.FIRE, PokemonType.WATER, PokemonType.ICE],
        [],
    ],
    PokemonType.BUG: [
        [PokemonType.GRASS, PokemonType.PSYCHIC],
        [PokemonType.FIRE, PokemonType.FIGHTING, PokemonType.POISON, PokemonType.FLYING, PokemonType.GHOST],
        [],
    ],
    PokemonType.DRAGON: [
        [PokemonType.DRAGON],
        [],
        [],
    ],
    PokemonType.POISON: [
        [PokemonType.GRASS],
        [PokemonType.POISON, PokemonType.GROUND, PokemonType.ROCK, PokemonType.GHOST],
        [],
    ],
    PokemonType.FLYING: [
        [PokemonType.GRASS, PokemonType.FIGHTING, PokemonType.BUG],
        [PokemonType.ELECTRIC, PokemonType.ROCK],
        [PokemonType.GROUND],
    ],
    PokemonType.GROUND: [
        [PokemonType.FIRE, PokemonType.ELECTRIC, PokemonType.POISON, PokemonType.ROCK],
        [PokemonType.WATER, PokemonType.ICE, PokemonType.GRASS],
        [],
    ],
    # Add more types as needed
}
        
        
BUFF_MULTIPLIERS = {
    -6: 0.4, -5: 0.5, -4: 0.6, -3: 0.7, -2: 0.8, -1: 0.9,
    0: 1.0,
    1: 1.1, 2: 1.2, 3: 1.3, 4: 1.4, 5: 1.5, 6: 1.6
}