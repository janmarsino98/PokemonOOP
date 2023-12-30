class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = [None] * 6
        self.inbattlefieldpokemon = None
        
    def set_pokemon(self, index, pokemon):
        if 0 <= index <= len(self.pokemons):
            self.pokemons[index] = pokemon
        
        else:
            print(f"The index {index} is not valid. Please introduce a number between 0 and {len(self.pokemons)}")
            
    def get_pokemon(self, index):
        if 0 <= index <= len(self.pokemons):
            return self.pokemons[index]
        
        else:
            print(f"The index {index} is not valid. Please select a number between 0 and 5.")
            
    def has_active_pokemon(self):
        return any(pokemon is not None and pokemon.is_alive() for pokemon in self.pokemons)
    
    def set_battlefield_pokemon(self, pokemon):
        self.inbattlefieldpokemon = pokemon
        print(f"{self.name} pokemon is now {pokemon.name}.")