from .pokemon import Pokemon

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
        print(f"{self.name}'s pokemon is now {pokemon.name}.")
        
    def select_movement(self):
        if isinstance(self.inbattlefieldpokemon, Pokemon):
            print(f"Select which movement will {self.inbattlefieldpokemon.name} will use: ")
            for n, movement in enumerate(self.inbattlefieldpokemon.movements):
                if movement is not None:
                    print(f"{n+1}. {movement.name}")
                else:
                    print(f"{n+1}. No movement")
                    
            chosen_movement = 0
            while chosen_movement not in range(1, len(self.inbattlefieldpokemon.movements)+1) or self.inbattlefieldpokemon.movements[chosen_movement-1] is None:
                try:
                    chosen_movement = int(input("Your choice: "))
                    
                except:
                    print("Invalid input. Please try again with a valid movement number.")
            
            print(f"The chosen movement was {self.inbattlefieldpokemon.movements[chosen_movement-1].name}")
            return self.inbattlefieldpokemon.movements[chosen_movement-1]
        
        else:
            print("You are not able to select a movement because you don't have a valid pokemon")
            exit()
            
    def select_target(self, own_pokemon, enemy_pokemon):
        while True:
            print("Choose a target for the movement:")
            print(f"1. Own pokemon: {own_pokemon.name}")
            print(f"2. Enemy pokemon: {enemy_pokemon.name}")
            chosen_pokemon_number = input("Your choice: ")
            if chosen_pokemon_number == "1":
                return own_pokemon
            elif chosen_pokemon_number == "2":
                return enemy_pokemon
            else:
                print("Your choice is not correct.")