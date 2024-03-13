from .trainer import Trainer
from .pokemon import Pokemon
from .movement import Movement
from .targetype import *

class Battle:
    def __init__(self, trainer1: Trainer, trainer2: Trainer):
        self.turn = 0
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        
    def start_turn(self):
        
        """Starts a new turn by adding 1 to the variable turn
        
        Args:
            - self: Instance of Battle
        
        Returns:
            None
        
        Comments:
            - Informs the user of the current turn
        """
        self.turn += 1
        print(f"Starting turn {self.turn}")
        print(f"**************************")
        
    def end_turn(self):
        
        """Informs the user that the current turn ended.
        
        Args:
            - self: Instance of Batle
            
        Returns:
            None
        """
        print(f"The turn {self.turn} ended.")
        
            
    def determine_winner(self):
        
        """Determines if there is an actual winner of a battle

        Args:
            - self: An instance of Batle
        Returns:
            winner(str): The name of the actual winner / None if there is no winner
        """
        
        if not self.trainer1.has_active_pokemon() and not self.trainer2.has_active_pokemon():
            print(f"The battle ended in a draw since none of the player have a pokemon alive.")
            winner = "Ninguno"
            
        elif not self.trainer1.has_active_pokemon():
            print(f"The winner is {self.trainer2.name}.")
            winner = self.trainer2.name
            
        elif not self.trainer2.has_active_pokemon():
            print(f"The winner is {self.trainer1.name}.")
            winner = self.trainer1.name
            
        else:
            print("There is no winner yet.")
            winner = None
            
        return winner
            
        
    def battle_loop(self):
        
        """Keeps starting and ending turns while there is no combat winner
        
        Args:
            - self: Instance of Battle
        
        Returns:
            None
            
        Comments:
            - The first turn it adds the first pokemon of each trainer to the battlefield
            - Every other turn, if there is no winner, the trainer must choose a movement.
            - If the chosen movement can be either used on itself or the enemy, the trainer will have to select a target also 
        """
          
        while self.trainer1.has_active_pokemon() and self.trainer2.has_active_pokemon():
            self.start_turn()
            
            if self.turn == 1:
                self.trainer1.set_battlefield_pokemon(self.trainer1.pokemons[0])
                self.trainer2.set_battlefield_pokemon(self.trainer2.pokemons[0])
                
            if self.determine_winner() is None:
                print(f"{self.trainer1.name} needs to select which movement is {self.trainer1.inbattlefieldpokemon.name} going to use")
                chosen_movenent = self.trainer1.select_movement(self.trainer1.inbattlefieldpokemon)
                target = None

                if chosen_movenent.default_target == TargetType.OWN:
                    target = self.trainer1.inbattlefieldpokemon
                elif chosen_movenent.default_target == TargetType.ENEMY:
                    target = self.trainer2.inbattlefieldpokemon
                elif chosen_movenent.default_target == TargetType.CHOOSE:
                    target = self.trainer1.select_target(self.trainer1.inbattlefieldpokemon, self.trainer2.inbattlefieldpokemon)
                if target is not None:
                    print(f"{self.trainer1.name}'s {self.trainer1.inbattlefieldpokemon.name} used {chosen_movenent.name} on {target.name}")
                    self.trainer1.inbattlefieldpokemon.attack_enemy(chosen_movenent, target)
                    
                else:
                    print("No valid target for the movement.")
                        
                
            
            else:
                self.determine_winner()
                
            self.end_turn()  
    
    def execute_movement(self, user_pokemon: Pokemon, enemy_pokemon: Pokemon, movement: Movement):
        user_pokemon.attack_enemy(movement, enemy_pokemon)
        
            
        
    def apply_movement_effects(self, user_pokemon: Pokemon, enemy_pokemon: Pokemon, movement: Movement):
        
        """Executes each effects of a certain movement when a pokemon uses it
        
        Args:
            - self: An instace of Battle
            - user_pokemon(Pokemon): The Pokemon that used the movement
            - enemy_pokemon(Pokemon): The Pokeomn that used the movement
            - movement(Movement): The movement that was used
            
        Returns:
            None
            
        Comments:
            - For each effect, first sets the target and then executes the effect
        """
        for effect in movement.effects:
            if effect.target == TargetType.OWN:
                target = user_pokemon
            elif effect.target == TargetType.ENEMY:
                target = enemy_pokemon
            elif effect.target == TargetType.CHOOSE:
                "target ="  #Implementar la resta de targets (se li hauria de passar el parametre des del target de la funció battle_loop)
                print("The target is not OWN nor ENEMY so the user should decide the target")
                
            if isinstance(effect, StatChangeEffect):
                print("OK")