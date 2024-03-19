from .trainer import Trainer
from .pokemon import Pokemon
from .movement import Movement
from .targetype import *
from .effect import *


class Battle:
    def __init__(self, trainer1: Trainer, trainer2: Trainer):
        self.turn = 0
        self.trainer1 = trainer1
        self.trainer2 = trainer2
            
    def determine_winner(self):
        
        """Determines if there is an actual winner of a battle

        Args:
            - self: An instance of Batle
        Returns:
            winner(str): The name of the actual winner / None if there is no winner
        """
        
        if len(self.trainer1.get_alive_pokemons()) == 0 and len(self.trainer2.get_alive_pokemons()) == 0:
            winner = "Draw"
            
        elif len(self.trainer1.get_alive_pokemons()) == 0:
            winner = self.trainer2
        elif len(self.trainer2.get_alive_pokemons()) == 0:
            winner = self.trainer1
        
        else:
            winner = None
            
        if winner:
            if winner == "Draw":
                return "None of the players has any pokemons alive so the battle resulted in a draw."
                
            else:
                return f"{winner.name} won the battle!"
        
        else:
            return
                
            
    def run_first_turn(self) -> None:
        
        """
        Runs the first turn of a battle which means setting each player's first pokemon to the battlefield
        
        Args:
            self: Instance of Battle
            
        Returns:
            None
        """
        
        self.trainer1.set_battlefield_pokemon(self.trainer1.pokemons[0])
        self.trainer2.set_battlefield_pokemon(self.trainer2.pokemons[0])
        self.turn += 1
        print("*"*40)
        
    def run_turn(self):
        turn_movements = []
        print(f"Starting turn {self.turn}...")
        print("-"*40)
        selected_movement = self.trainer1.inbattlefieldpokemon.select_movement()
        priority_move = False
        for effect in selected_movement.effects:
            if effect["category"] == EffectCategory.PRIORITY:
                priority_move = True
                break
            
        if priority_move == True:
            turn_movements.insert(0, [selected_movement, self.trainer1.inbattlefieldpokemon, self.trainer1.inbattlefieldpokemon.speed, self.trainer2.inbattlefieldpokemon])
        else:
            turn_movements.append([selected_movement, self.trainer1.inbattlefieldpokemon, self.trainer1.inbattlefieldpokemon.speed, self.trainer2.inbattlefieldpokemon])
            
            
        selected_movement = self.trainer2.inbattlefieldpokemon.select_movement()
        priority_move = False
        for effect in selected_movement.effects:
            if effect["category"] == EffectCategory.PRIORITY:
                priority_move = True
                break
        if priority_move == True:
            turn_movements.insert(0, [selected_movement, self.trainer2.inbattlefieldpokemon, self.trainer2.inbattlefieldpokemon.speed, self.trainer1.inbattlefieldpokemon])
        
        else:
            turn_movements.append([selected_movement, self.trainer2.inbattlefieldpokemon, self.trainer2.inbattlefieldpokemon.speed, self.trainer1.inbattlefieldpokemon])
            
        for turn_movement in turn_movements:
            movement, user, speed, target = turn_movement
            user.use_movement(movement, target)
            winner = self.determine_winner()
            if winner:
                print(winner)
                exit()
                

        self.turn += 1
        print("*"*40)